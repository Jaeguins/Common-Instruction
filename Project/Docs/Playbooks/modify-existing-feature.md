# Playbook: 기존 기능 수정

## When To Use
이미 존재하는 기능의 동작을 변경할 때 사용한다.

## Required Reading
- `../ProjectRules/architecture-policy.md`
- 작업 경로 상위의 `CONTEXT.md`, `ADR-Refs.md`(있는 경우)

## Procedure
1. 현재 동작과 의존하는 호출부를 파악한다.
2. 변경이 되돌리기 어려운지, 외부 계약(저장/네트워크/공개 API)에 영향을 주는지 확인한다.
3. 하위 호환이 필요하면 마이그레이션/버전 처리를 포함한다.
4. 최소 범위로 변경하고 동작 차이를 명확히 한다.

## Validation
- 기존 테스트가 통과하는지 확인한다.
- 변경된 동작에 대한 테스트를 추가/갱신한다.

## Output
- 변경 코드 + 테스트
- 동작 변경 요약
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `./add-new-feature.md`
- `./refactor-code.md`
