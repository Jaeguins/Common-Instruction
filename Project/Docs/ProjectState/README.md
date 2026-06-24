# ProjectState — 현재 프로젝트 상태

이 폴더는 자주 바뀌는 **현재 상태**를 기록한다.
안정적인 규칙은 여기 두지 않는다(→ `../ProjectRules/`).

## 상태 문서 기준

- 각 문서는 아래 공통 형식을 따른다.
- 이 템플릿에는 실제 마일스톤/피쳐 내용을 쓰지 않는다. 프로젝트 생성 후 사람이 채운다.
- 상태가 바뀌면 즉시 갱신하고 `Last Updated`를 기록한다.

## 공통 형식

```md
# 문서 제목

## Current Summary
현재 상태 요약을 작성한다.

## Active Priorities
현재 우선순위를 작성한다.

## Constraints
현재 작업 시 주의해야 할 제약을 작성한다.

## Open Questions
아직 결정되지 않은 사항을 작성한다.

## Last Updated
최종 갱신일을 작성한다.
```

## 포함 문서

- `milestone-current.md` — 현재 마일스톤
- `sprint-current.md` — 현재 스프린트
- `feature-current.md` — 현재 개발 피쳐
- `known-issues.md` — 알려진 문제
- `tech-debt.md` — 기술부채 목록
- `temporary-workarounds.md` — 임시 우회 목록
- `qa-focus.md` — QA 집중 항목
- `build-status.md` — 빌드 상태 요약
