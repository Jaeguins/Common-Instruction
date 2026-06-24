#!/usr/bin/env python3
"""Markdown 문서의 상대 링크/참조 경로가 실제로 존재하는지 점검한다.

선택 검증 도구다. 일반 작업 완료 루틴에서 자동 실행하지 않는다.
표준 라이브러리만 사용한다.

점검 대상:
- Markdown 상대 링크의 대상 경로 존재 여부
- ADR-Refs.md가 /Docs/Decisions 아래 ADR을 참조하는지

placeholder(예: ADR-SCOPE-0000, <this-directory>)와 Docs/Templates 내부는
의도된 미완성 상태이므로 점검에서 제외한다.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# 이 스크립트는 Project/Tools/ 에 위치한다. 프로젝트 루트는 그 부모다.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_TOKENS = ("0000", "SCOPE", "<", ">", "TODO", "ADR-SCOPE")
SKIP_DIRS = {"Templates"}


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def has_placeholder(target: str) -> bool:
    return any(tok in target for tok in PLACEHOLDER_TOKENS)


def resolve(md_file: Path, target: str) -> Path:
    target = target.split("#", 1)[0].strip()
    if target.startswith("/"):
        return (PROJECT_ROOT / target.lstrip("/")).resolve()
    return (md_file.parent / target).resolve()


def iter_markdown_files():
    for path in PROJECT_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(PROJECT_ROOT).parts):
            continue
        yield path


def main() -> int:
    problems: list[str] = []
    checked = 0

    for md in iter_markdown_files():
        text = md.read_text(encoding="utf-8")
        rel_md = md.relative_to(PROJECT_ROOT)
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if not target or is_external(target) or has_placeholder(target):
                continue
            checked += 1
            resolved = resolve(md, target)
            if not resolved.exists():
                problems.append(f"{rel_md}: 링크 대상 없음 -> {target}")

        # ADR-Refs.md는 /Docs/Decisions 아래 ADR만 참조해야 한다.
        if md.name == "ADR-Refs.md":
            for line in text.splitlines():
                ref = line.strip().lstrip("- ").strip()
                if ref.startswith("/Docs/") and ref.endswith(".md"):
                    if not ref.startswith("/Docs/Decisions/"):
                        problems.append(
                            f"{rel_md}: ADR 참조가 /Docs/Decisions 밖을 가리킴 -> {ref}"
                        )

    print(f"[validate-doc-links] 검사한 링크: {checked}, 문제: {len(problems)}")
    for p in problems:
        print(f"  - {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
