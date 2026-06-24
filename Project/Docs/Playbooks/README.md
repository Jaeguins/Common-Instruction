# Playbooks — 작업별 절차서

이 폴더는 작업 유형별 **범용 절차서**를 담는다.
특정 엔진/코드베이스에 종속된 실제 클래스명·경로·시스템명은 쓰지 않는다.

## 플레이북 기준

- 각 플레이북은 아래 공통 형식을 따른다.
- 범용 절차만 작성한다. 프로젝트별 세부는 ProjectRules와 CONTEXT를 참조하도록 링크만 둔다.
- 작업 유형 ↔ 플레이북 매핑은 `/AGENTS.md`의 라우팅 표를 기준으로 한다.

## 공통 형식

```md
# Playbook Title

## When To Use
이 플레이북을 사용할 상황을 작성한다.

## Required Reading
작업 전 읽어야 하는 문서 경로를 작성한다.

## Procedure
작업 절차를 단계별로 작성한다.

## Validation
자동/수동 검증 방법을 작성한다.

## Output
작업 후 남겨야 할 산출물을 작성한다.

## Related Documents
관련 규칙, 상태 문서, ADR 경로를 작성한다.
```

## 포함 문서 (범용 작업 유형)

기본 템플릿에는 특정 시스템명이 아닌 범용 작업 유형 중심의 플레이북만 둔다.

- `add-new-feature.md` — 신규 기능 추가
- `modify-existing-feature.md` — 기존 기능 수정
- `refactor-code.md` — 리팩터링
- `investigate-bug.md` — 버그 조사
- `investigate-crash.md` — 크래시 조사
- `optimize-performance.md` — 성능 최적화
- `add-or-update-test.md` — 테스트 추가/수정
- `update-content-or-data.md` — 콘텐츠/데이터 갱신
- `update-build-or-release.md` — 빌드/릴리즈 변경
- `update-documentation.md` — 문서 갱신

## 프로젝트별 플레이북 추가 기준

프로젝트에 UI, 로컬라이징, 네트워크, 저장, 데이터테이블, 플랫폼별 빌드, 에셋 번들 등
특수 영역 절차가 필요하면 해당 플레이북을 **그때 추가**한다.
기본 템플릿은 이런 절차를 미리 생성하지 않는다.
