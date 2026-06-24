#!/usr/bin/env python3
"""에이전트 지침 템플릿의 기본 구조가 유지되고 있는지 점검한다.

선택 검증 도구다. 일반 작업 완료 루틴에서 자동 실행하지 않는다.
표준 라이브러리만 사용한다.
"""
from __future__ import annotations

import sys
from pathlib import Path

# 이 스크립트는 Project/Tools/ 에 위치한다. 프로젝트 루트는 그 부모다.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "AGENTS.md",
    "Docs/README.md",
    "Docs/ProjectRules/README.md",
    "Docs/Playbooks/README.md",
    "Docs/Templates/README.md",
    "Docs/Decisions/ADR-TEMPLATE.md",
    "Docs/Governance/CHANGE-TEMPLATE.md",
    "Docs/Validation/manual-checklist.md",
]


def main() -> int:
    missing = [rel for rel in REQUIRED_FILES if not (PROJECT_ROOT / rel).exists()]

    print(
        f"[validate-agent-docs] 필수 파일 {len(REQUIRED_FILES)}개 중 "
        f"누락 {len(missing)}개"
    )
    for rel in missing:
        print(f"  - 누락: {rel}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
