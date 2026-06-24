# Playbook: 크래시 조사

## When To Use
크래시나 치명적 오류를 조사할 때 사용한다.

## Required Reading
- `../ProjectState/known-issues.md`
- `../ProjectRules/testing-policy.md`

## Procedure
1. 재현 조건과 빈도, 영향 범위를 수집한다.
2. 로그/스택트레이스/덤프를 확보한다.
3. 최근 변경과 연관성을 확인한다.
4. 최소 재현 케이스를 만든다.
5. 원인을 수정하거나 임시 우회를 적용한다.

## Validation
- 최소 재현 케이스가 더 이상 크래시하지 않는지 확인한다.
- 회귀 테스트를 추가한다.

## Output
- 수정 또는 우회 적용
- `../ProjectState/known-issues.md` / `temporary-workarounds.md` 갱신
- `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `./investigate-bug.md`
- `../ProjectState/known-issues.md`
- `../ProjectState/temporary-workarounds.md`
