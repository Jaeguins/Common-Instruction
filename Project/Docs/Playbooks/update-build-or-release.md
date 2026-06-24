# Playbook: 빌드/릴리즈 변경

## When To Use
빌드 설정, 릴리즈 파이프라인, 패키징을 변경할 때 사용한다.

## Required Reading
- `../ProjectState/build-status.md`
- 프로젝트에 플랫폼/빌드 규칙 문서가 있으면 함께 읽는다.

## Procedure
1. 변경 목적과 영향 받는 플랫폼/환경을 식별한다.
2. 되돌리기 어려운 변경인지, 외부 배포에 영향을 주는지 확인한다.
3. 변경 후 클린 빌드로 재현되는지 확인한다.
4. 다른 플랫폼/환경에 영향이 없는지 확인한다.

## Validation
- 대상 환경에서 클린 빌드가 성공하는지 확인한다.
- 릴리즈 산출물이 기대대로인지 확인한다.

## Output
- 빌드/릴리즈 설정 변경
- `../ProjectState/build-status.md` 갱신
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `../ProjectState/build-status.md`
