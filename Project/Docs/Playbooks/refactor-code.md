# Playbook: 리팩터링

## When To Use
동작을 바꾸지 않고 코드 구조/가독성/구성을 개선할 때 사용한다.

## Required Reading
- `../ProjectRules/architecture-policy.md`
- `../ProjectRules/coding-convention.md`

## Procedure
1. 리팩터링 전 동작을 보장할 테스트/기준을 확보한다.
2. 책임 단위로 경계를 식별한다.
3. 의존성 방향을 지키며 단계적으로 변경한다.
4. 동작 변경 없이 구조만 바꾸는지 확인한다.

## Validation
- 기존 테스트가 모두 통과하는지 확인한다.
- 동작이 동일한지 검증한다.

## Output
- 개선된 구조
- 영향받은 `CONTEXT.md` 갱신
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `../ProjectRules/architecture-policy.md`
- `./modify-existing-feature.md`
