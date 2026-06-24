# Playbook: 콘텐츠/데이터 갱신

## When To Use
게임 데이터, 설정, 콘텐츠 등 데이터성 자산을 추가·갱신할 때 사용한다.

## Required Reading
- 작업 경로 상위의 `CONTEXT.md`, `ADR-Refs.md`(있는 경우)
- 프로젝트에 데이터/콘텐츠 규칙 문서가 있으면 함께 읽는다.

## Procedure
1. 변경 대상 데이터와 영향 범위를 식별한다.
2. 정의된 형식/스키마와 무결성 규칙을 지킨다.
3. 버전/마이그레이션이 필요한지 확인한다.
4. 런타임 로딩/참조에 문제가 없는지 확인한다.

## Validation
- 데이터 무결성/로딩을 검증한다.
- 관련 기능이 정상 동작하는지 확인한다.

## Output
- 데이터/콘텐츠 변경
- 영향도가 크면 `../WorkLogs/`에 작업 로그 기록

## Related Documents
- `./add-new-feature.md`
