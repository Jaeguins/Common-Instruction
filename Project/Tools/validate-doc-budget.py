#!/usr/bin/env python3
"""항상 읽히는 문서의 크기 예산과 폐기 ADR 잔존 참조를 정적으로 점검한다.

선택 검증 도구다. 일반 작업 완료 루틴에서 자동 실행하지 않는다.
표준 라이브러리만 사용한다.

점검 대상(정적으로 명확한 것만):
- CONTEXT.md  : 줄 수가 예산(CONTEXT_MAX_LINES)을 넘는지
- ADR-Refs.md : 활성 ADR 참조 수가 예산(ADR_REFS_MAX_ACTIVE)을 넘는지
- ADR-Refs.md : 참조 대상 ADR 원문의 Status가 Deprecated/Superseded인데
                참조가 남아 있는지(폐기 잔존 참조)

기준 근거: Docs/ProjectRules/documentation-policy.md
Docs/Templates 내부는 의도된 예시/placeholder이므로 점검에서 제외한다.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# 이 스크립트는 Project/Tools/ 에 위치한다. 프로젝트 루트는 그 부모다.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# documentation-policy.md의 권장 상한과 일치시킨다.
CONTEXT_MAX_LINES = 40
ADR_REFS_MAX_ACTIVE = 15

SKIP_DIRS = {"Templates"}
PLACEHOLDER_TOKENS = ("0000", "SCOPE", "<", ">", "TODO")
DEPRECATED_TOKENS = ("Deprecated", "Superseded")

ADR_REF_RE = re.compile(r"/Docs/Decisions/[^\s)]+\.md")


def has_placeholder(text: str) -> bool:
    return any(tok in text for tok in PLACEHOLDER_TOKENS)


def iter_files(name: str):
    for path in PROJECT_ROOT.rglob(name):
        if any(part in SKIP_DIRS for part in path.relative_to(PROJECT_ROOT).parts):
            continue
        yield path


def adr_status(adr_path: Path) -> str:
    """ADR 원문의 ## Status 본문을 한 줄로 돌려준다. 없으면 빈 문자열."""
    if not adr_path.exists():
        return ""
    lines = adr_path.read_text(encoding="utf-8").splitlines()
    collecting = False
    body: list[str] = []
    for line in lines:
        if line.strip().lower() == "## status":
            collecting = True
            continue
        if collecting:
            if line.startswith("## "):  # 다음 섹션 시작
                break
            stripped = line.strip()
            if not stripped or stripped.startswith("<!--") or stripped.startswith("-->"):
                continue
            body.append(stripped)
    return " ".join(body)


def main() -> int:
    problems: list[str] = []
    checked = 0

    # 1. CONTEXT.md 줄 수 예산
    for ctx in iter_files("CONTEXT.md"):
        checked += 1
        line_count = len(ctx.read_text(encoding="utf-8").splitlines())
        if line_count > CONTEXT_MAX_LINES:
            rel = ctx.relative_to(PROJECT_ROOT)
            problems.append(
                f"{rel}: 줄 수 예산 초과 ({line_count} > {CONTEXT_MAX_LINES}). "
                f"디렉토리 분할/내용 축소를 검토한다."
            )

    # 2. ADR-Refs.md 활성 참조 수 + 폐기 잔존 참조
    for refs in iter_files("ADR-Refs.md"):
        checked += 1
        rel = refs.relative_to(PROJECT_ROOT)
        text = refs.read_text(encoding="utf-8")

        active_refs: list[str] = []
        for m in ADR_REF_RE.finditer(text):
            target = m.group(0)
            if has_placeholder(target):
                continue
            active_refs.append(target)

        if len(active_refs) > ADR_REFS_MAX_ACTIVE:
            problems.append(
                f"{rel}: 활성 ADR 참조 수 예산 초과 "
                f"({len(active_refs)} > {ADR_REFS_MAX_ACTIVE}). "
                f"규칙 push-down/디렉토리 분할을 검토한다."
            )

        for target in active_refs:
            adr_path = (PROJECT_ROOT / target.lstrip("/")).resolve()
            status = adr_status(adr_path)
            if any(tok in status for tok in DEPRECATED_TOKENS):
                problems.append(
                    f"{rel}: 폐기된 ADR을 참조 중 (Status: {status.strip()}) -> {target}. "
                    f"참조를 제거한다(원문은 Decisions에 보존)."
                )

    print(f"[validate-doc-budget] 검사한 문서: {checked}, 문제: {len(problems)}")
    for p in problems:
        print(f"  - {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
