# Playbook: 신규 기능 추가

## When To Use
새로운 기능을 추가할 때 사용한다.

## Required Reading
- `../ProjectRules/architecture-policy.md`
- `../ProjectRules/coding-convention.md`
- 작업 경로 상위의 `CONTEXT.md`, `AGENTS.md`, `ADR-Refs.md`(있는 경우)

## Procedure
1. 기능의 책임과 경계를 정의한다.
2. 구조 정책에 맞는 배치와 의존성 방향을 정한다.
3. 코딩 컨벤션에 맞게 구현한다.
4. 외부에 영향을 주는 인터페이스(저장/네트워크/공개 API)는 영향도를 명시한다.
5. 영향이 크면 ADR 추가를 검토한다.

## Validation
- 관련 테스트를 추가/실행한다(`../ProjectRules/testing-policy.md`).
- 영향 범위에 회귀가 없는지 확인한다.

## Output
- 기능 코드 + 필요한 테스트
- 영향받은 `CONTEXT.md` 갱신
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `./modify-existing-feature.md`
- `./add-or-update-test.md`
