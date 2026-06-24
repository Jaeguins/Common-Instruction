# WorkLogs — 작업 결과 기록

이 폴더는 작업 완료 후 결과를 기록한다.
보고 형식은 `/AGENTS.md`의 작업 완료 보고 형식과 일치한다.

## 작업 로그 기준 (영향도 중심)

WorkLog는 모든 작업에 반드시 남기지 않는다. 다만 다음에 해당하면 남기는 것을 권장한다.

- 변경 이유와 결과를 후속 작업자가 알아야 하는 경우
- 되돌리기 어렵거나 영향 범위가 넓은 경우
- 전역 규칙, Playbook, ADR, CONTEXT가 갱신된 경우
- 검증 결과나 리스크를 명시해야 하는 경우
- 임시 우회 또는 기술부채가 추가된 경우

즉 "큰 작업"은 고정 수치가 아니라 **영향도 기준**으로 판단한다.

## 파일명 규칙

```text
YYYY-MM-DD-short-topic.md
YYYY-MM-DD-001-short-topic.md
```

프로젝트별로 다른 명명 규칙이 필요하면 이 README에서 변경할 수 있다.

## 작성 방법

- `WORKLOG-TEMPLATE.md`를 복사해 새 로그를 작성한다.
- 갱신한 ProjectState/CONTEXT/ADR 문서를 기록한다.

## 포함 문서

- `WORKLOG-TEMPLATE.md` — 작업 로그 템플릿
