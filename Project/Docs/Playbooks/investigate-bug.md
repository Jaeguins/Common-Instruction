# Playbook: 버그 조사

## When To Use
잘못된 동작이나 기능 결함을 조사·수정할 때 사용한다. (치명적 크래시는 `./investigate-crash.md`)

## Required Reading
- `../ProjectState/known-issues.md`
- `../ProjectRules/testing-policy.md`

## Procedure
1. 재현 조건과 기대/실제 동작을 명확히 한다.
2. 최소 재현 케이스를 만든다.
3. 최근 변경과의 연관성을 확인한다.
4. 원인을 수정하거나, 불가하면 임시 우회를 적용하고 기록한다.

## Validation
- 재현 케이스가 해소되는지 확인한다.
- 회귀 테스트를 추가한다.

## Output
- 수정 또는 우회
- `../ProjectState/known-issues.md` / `temporary-workarounds.md` 갱신
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `./investigate-crash.md`
- `./add-or-update-test.md`
