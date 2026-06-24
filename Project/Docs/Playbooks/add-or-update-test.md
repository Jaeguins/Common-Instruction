# Playbook: 테스트 추가/수정

## When To Use
테스트를 추가하거나 기존 테스트를 갱신할 때 사용한다.

## Required Reading
- `../ProjectRules/testing-policy.md`

## Procedure
1. 검증할 동작과 테스트 종류(단위/통합/기타)를 정한다.
2. 테스트 정책에 맞는 위치/명명으로 작성한다.
3. 실패가 의미 있는지(거짓 통과가 아닌지) 확인한다.

## Validation
- 테스트가 통과/실패를 올바르게 판별하는지 확인한다.
- 기존 테스트에 영향이 없는지 확인한다.

## Output
- 추가/수정된 테스트
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `../ProjectRules/testing-policy.md`
- `./investigate-bug.md`
