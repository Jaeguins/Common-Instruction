너는 LLM Agent용 프로젝트 지침 템플릿 레포지토리를 생성하는 에이전트다.

목표는 특정 프로젝트에 종속되지 않고, 어떤 게임 개발 프로젝트든 새로 시작할 때 복사해서 사용할 수 있는 범용 지침 템플릿을 만드는 것이다.

아래 조건에 맞춰 현재 레포지토리 안에 `Project/` 폴더를 만들고, 그 안에 에이전트 지침 템플릿 파일과 디렉토리 구조를 생성하라.

---

# 핵심 원칙

1. 이 템플릿은 특정 프로젝트의 실제 기획, 아키텍처, 코드 구조, 마일스톤을 포함하지 않는다.
2. 프로젝트별로 달라질 수 있는 내용은 직접 작성하지 말고, “해당 내용은 어느 경로의 문서에 작성한다”는 전역 규칙으로만 남긴다.
3. 루트 지침 파일은 세부 내용을 모두 담는 문서가 아니라, 필요한 문서로 안내하는 라우터 역할을 해야 한다.
4. 지침은 작업 요청보다 우선한다. 단, 사용자가 지침 자체의 변경을 명시적으로 요청한 경우에는 Governance Change로 취급한다.
5. ADR 원문은 전역 위치에 모으고, 영향을 받는 디렉토리에는 `ADR-Refs.md`로 참조만 둔다.
6. 디렉토리별 `CONTEXT.md`는 코드 전체 설명서가 아니라, 에이전트가 빠르게 탐색하기 위한 짧은 지도여야 한다.
7. 모든 템플릿 문서는 실제 프로젝트 내용 대신 작성 가이드, 예시, TODO, placeholder를 포함한다.
8. 생성되는 “전체 구조 예시”에는 각 줄 뒤에 30자 이내의 1줄 설명을 같은 줄에 붙인다.

---

# 생성할 최상위 구조

`Project/` 아래에 다음 구조를 생성하라.

```text
Project/                                      # 프로젝트 템플릿 루트
  AGENTS.md                                  # 공통 에이전트 진입점
  CLAUDE.md                                  # Claude용 진입점
  .cursorrules                               # Cursor용 진입점
  .github/                                   # GitHub 설정
    copilot-instructions.md                  # Copilot용 지침
    pull_request_template.md                 # PR 보고 템플릿

  Docs/                                      # 지침 문서 루트
    README.md                                # 지침 체계 설명

    ProjectRules/                            # 안정 전역 규칙
      README.md                              # 규칙 작성 기준
      coding-convention.md                   # 코드 스타일 원칙
      architecture-policy.md                 # 구조 설계 원칙
      ui-policy.md                           # UI 구현 원칙
      localization-policy.md                 # 로컬라이징 원칙
      data-table-policy.md                   # 데이터 구조 원칙
      save-data-policy.md                    # 저장 데이터 원칙
      network-policy.md                      # 네트워크 원칙
      asset-pipeline-policy.md               # 에셋 파이프라인
      addressables-policy.md                 # 번들/주소 정책
      platform-android-policy.md             # Android 정책
      platform-ios-policy.md                 # iOS 정책
      testing-policy.md                      # 테스트 기준
      performance-policy.md                  # 성능 판단 기준

    ProjectState/                            # 현재 프로젝트 상태
      README.md                              # 상태 문서 기준
      milestone-current.md                   # 현재 마일스톤
      sprint-current.md                      # 현재 스프린트
      feature-current.md                     # 현재 개발 피쳐
      known-issues.md                        # 알려진 문제
      tech-debt.md                           # 기술부채 목록
      temporary-workarounds.md               # 임시 우회 목록
      qa-focus.md                            # QA 집중 항목
      build-status.md                        # 빌드 상태 요약

    Playbooks/                               # 작업별 절차서
      README.md                              # 플레이북 기준
      add-new-ui-screen.md                   # 신규 UI 절차
      add-new-localized-text.md              # 로컬라이징 절차
      add-new-data-table.md                  # 데이터 추가 절차
      add-new-editor-tool.md                 # 에디터툴 절차
      add-new-network-message.md             # 네트워크 메시지
      add-new-save-field.md                  # 저장 필드 추가
      investigate-crash.md                   # 크래시 조사
      optimize-mobile-memory.md              # 메모리 최적화
      refactor-large-file.md                 # 대형 파일 분리
      fix-platform-build-error.md            # 플랫폼 빌드 오류
      update-bundled-content.md              # 번들 콘텐츠 갱신

    Decisions/                               # ADR 원문 저장소
      README.md                              # ADR 작성 기준
      ADR-TEMPLATE.md                        # ADR 템플릿
      ADR-EXAMPLE-0001.md                    # ADR 예시

    WorkLogs/                                # 작업 결과 기록
      README.md                              # 작업 로그 기준
      WORKLOG-TEMPLATE.md                    # 작업 로그 템플릿

  Source/                                    # 코드 루트 예시
    CONTEXT.md                               # 코드 루트 지도
    AGENTS.md                                # 코드 로컬 지침
    ADR-Refs.md                              # 관련 결정 링크

  Assets/                                    # 에셋 루트 예시
    CONTEXT.md                               # 에셋 루트 지도
    AGENTS.md                                # 에셋 로컬 지침
    ADR-Refs.md                              # 관련 결정 링크
```

---

# 각 파일 작성 방향

## `Project/AGENTS.md`

다음을 포함하라.

* 이 문서가 프로젝트 진입 지침이라는 설명
* 세부 규칙은 직접 담지 않고 `Docs/` 하위 문서로 라우팅한다는 원칙
* 지침 우선순위
* 충돌 처리 정책
* Governance Change 정책
* 작업 유형별 읽을 문서 목록
* 작업 완료 보고 형식
* 문서 갱신 의무
* ADR 참조 방식

지침 우선순위는 다음으로 작성하라.

```text
1. Safety / Tool / Platform Constraints
2. Project Entry Instructions
3. ProjectRules
4. Directory AGENTS.md
5. ProjectState
6. Playbooks
7. Directory CONTEXT.md
8. Session Request
9. Inferred Intent
```

단, 세션 요청이 명시적으로 지침 변경을 요구하는 경우에는 일반 작업 요청이 아니라 Governance Change로 처리한다고 명시하라.

Governance Change에는 다음을 포함하라.

```text
- 변경 대상 문서
- 기존 지침
- 변경 제안
- 영향 범위
- 필요한 후속 문서 갱신
- ADR 추가/수정 필요 여부
```

작업 완료 보고 형식은 다음으로 하라.

```text
1. 변경 요약
2. 수정 파일
3. 동작 변경
4. 검증 결과
5. 지침 충돌 여부
6. 리스크
7. 후속 작업
8. 갱신한 문서
```

---

## `Project/CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`

각 도구용 파일은 중복된 긴 지침을 담지 말고, 기본적으로 `AGENTS.md`를 따르도록 작성하라.

예:

```text
이 프로젝트의 표준 에이전트 지침은 /AGENTS.md를 기준으로 한다.
작업 전 /AGENTS.md를 먼저 확인하고, 작업 유형에 따라 필요한 Docs 문서를 읽는다.
```

도구별 특수 제약이 있다면 placeholder로만 남긴다.

---

## `Docs/ProjectRules/`

각 문서는 실제 프로젝트 규칙을 확정하지 말고, 어떤 내용을 이 파일에 작성해야 하는지 템플릿으로 작성하라.

각 파일은 다음 형식을 따른다.

```md
# 문서 제목

## Purpose

이 문서가 담당하는 범위를 설명한다.

## Stable Rules

프로젝트 전역에서 안정적으로 유지되어야 하는 규칙을 작성한다.

## Allowed Exceptions

예외가 가능하다면 어떤 기준으로 허용하는지 작성한다.

## Validation

이 규칙이 지켜졌는지 확인하는 방법을 작성한다.

## Related Documents

관련 ProjectRules, Playbooks, ADR 경로를 작성한다.
```

주의:

* 현재 프로젝트 고유 내용은 쓰지 않는다.
* 예시는 placeholder로만 둔다.
* “이 프로젝트에서는 반드시 X를 사용한다” 같은 확정 표현은 피하고, “해당 프로젝트에서 사용하는 방식을 여기에 작성한다”로 둔다.

---

## `Docs/ProjectState/`

자주 바뀌는 현재 상태를 기록하는 곳임을 설명하라.

각 파일은 다음 형식을 따른다.

```md
# 문서 제목

## Current Summary

현재 상태 요약을 작성한다.

## Active Priorities

현재 우선순위를 작성한다.

## Constraints

현재 작업 시 주의해야 할 제약을 작성한다.

## Open Questions

아직 결정되지 않은 사항을 작성한다.

## Last Updated

최종 갱신일을 작성한다.
```

주의:

* 이 템플릿에는 실제 마일스톤이나 피쳐 내용을 쓰지 않는다.
* 프로젝트 생성 후 사람이 채우도록 TODO를 남긴다.

---

## `Docs/Playbooks/`

작업 유형별 절차서를 작성하는 곳이다.

각 플레이북은 다음 형식을 따른다.

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

각 플레이북에는 범용적인 절차만 작성하고, 특정 프로젝트의 실제 클래스명, 경로, 시스템명은 쓰지 않는다.

---

## `Docs/Decisions/`

ADR 원문 저장소로 작성한다.

`README.md`에는 다음 원칙을 포함하라.

```text
- ADR 원문은 모두 /Docs/Decisions에 둔다.
- 영향을 받는 디렉토리에는 ADR-Refs.md로 링크만 둔다.
- ADR 원문을 디렉토리마다 중복 복사하지 않는다.
- 하나의 ADR이 여러 영역에 영향을 주면 각 영역 ADR-Refs.md에 참조를 추가한다.
- ADR 파일명은 영향 범위를 포함할 수 있다.
```

파일명 예시는 다음처럼 작성하라.

```text
ADR-DATA-0001-table-memory-layout.md
ADR-UI-0001-screen-navigation.md
ADR-NET-0001-message-versioning.md
ADR-SAVE-0001-save-versioning.md
ADR-PLATFORM-0001-android-build-policy.md
```

`ADR-TEMPLATE.md`는 다음 형식으로 작성하라.

```md
# ADR-SCOPE-0000-title

## Status

Proposed / Accepted / Deprecated / Superseded

## Context

이 결정을 하게 된 배경을 작성한다.

## Decision

채택한 결정을 작성한다.

## Alternatives Considered

검토했지만 선택하지 않은 대안을 작성한다.

## Consequences

이 결정으로 생기는 장단점을 작성한다.

## Affected Areas

영향받는 경로와 시스템을 작성한다.

## Do Not

에이전트가 되돌리면 안 되는 사항을 작성한다.

## Related Documents

관련 규칙, 플레이북, 컨텍스트 문서 경로를 작성한다.
```

---

## `Docs/WorkLogs/`

작업 완료 후 결과를 기록하는 곳이다.

`WORKLOG-TEMPLATE.md`는 다음 형식으로 작성하라.

```md
# Work Log: Title

## Summary

작업 요약을 작성한다.

## Changed Files

수정 파일을 작성한다.

## Behavior Changes

동작 변경을 작성한다.

## Validation Results

검증 결과를 작성한다.

## Instruction Conflicts

지침과 충돌한 사항이 있었는지 작성한다.

## Risks

남은 리스크를 작성한다.

## Follow-ups

후속 작업을 작성한다.

## Updated Documents

갱신한 지침/컨텍스트/ADR 문서를 작성한다.
```

---

## `Source/CONTEXT.md`, `Assets/CONTEXT.md`

디렉토리 컨텍스트 문서 템플릿을 작성하라.

형식은 다음과 같다.

```md
# Directory Context

## Responsibility

이 디렉토리가 담당하는 책임을 작성한다.

## Key Files

주요 파일과 역할을 작성한다.

## Subdirectories

하위 디렉토리와 역할을 작성한다.

## External Dependencies

외부 의존성을 작성한다.

## Local Rules

이 디렉토리에서만 중요한 주의사항을 작성한다.

## Validation

이 디렉토리 수정 후 확인할 검증 방법을 작성한다.

## Related Documents

관련 ProjectRules, Playbooks, ADR-Refs 경로를 작성한다.
```

주의:

* 디렉토리 컨텍스트는 현재 디렉토리와 바로 하위 디렉토리까지만 설명한다.
* 전체 프로젝트 설명을 반복하지 않는다.
* 코드 전문을 요약하지 않는다.
* 에이전트가 탐색을 시작할 수 있는 지도 수준으로만 작성한다.

---

## `Source/AGENTS.md`, `Assets/AGENTS.md`

로컬 지침 템플릿을 작성하라.

형식은 다음과 같다.

```md
# Local Agent Rules

## Scope

이 지침이 적용되는 경로를 작성한다.

## Local Rules

이 경로에서 반드시 지켜야 할 로컬 규칙을 작성한다.

## Required Reading

이 경로 작업 전 읽어야 할 문서를 작성한다.

## Conflict Policy

상위 지침과 충돌할 경우 상위 지침을 우선한다고 작성한다.

## Related ADRs

관련 ADR은 ADR-Refs.md를 확인하도록 작성한다.
```

---

## `Source/ADR-Refs.md`, `Assets/ADR-Refs.md`

로컬 ADR 참조 템플릿을 작성하라.

형식은 다음과 같다.

```md
# Related ADRs

이 경로에 영향을 주는 ADR을 참조한다.
ADR 원문은 /Docs/Decisions에 둔다.

- /Docs/Decisions/ADR-SCOPE-0000-title.md
  - 이 경로에 미치는 영향 요약.
  - 에이전트가 주의해야 할 사항.
```

---

# 최종 출력 요구사항

1. 위 구조대로 실제 파일과 폴더를 생성하라.
2. 각 파일에는 바로 사용할 수 있는 Markdown 템플릿 내용을 작성하라.
3. 특정 프로젝트에 종속된 내용은 넣지 말고 placeholder 또는 TODO로 남겨라.
4. `Project/Docs/README.md`에는 전체 지침 체계와 문서 계층 설명을 작성하라.
5. `Project/AGENTS.md`에는 에이전트가 실제 작업 시 따를 라우팅 규칙을 충분히 구체적으로 작성하라.
6. “전체 구조 예시” 코드블럭에는 각 줄 뒤에 30자 이내의 설명 주석을 붙여라.
7. 모든 문서는 한국어 기준으로 작성하라.
8. 파일 내용은 간결하지만 실제 운영 가능한 수준이어야 한다.
9. 중복 설명은 줄이고, 각 문서의 책임이 겹치지 않게 하라.
10. 작업 완료 후 생성한 파일 목록과 핵심 설계 판단을 요약하라.

---

# 특히 주의할 점

* `ProjectRules`에는 프로젝트별 실제 선택지를 쓰지 말고, 프로젝트별 규칙을 작성할 위치와 형식만 제공하라.
* `ProjectState`에는 실제 상태를 쓰지 말고, 상태를 기록할 템플릿만 제공하라.
* `Playbooks`에는 특정 엔진이나 코드베이스에 종속되지 않는 범용 절차를 작성하라.
* `Decisions`에는 ADR 원문을 모으고, 로컬에는 참조만 둔다는 원칙을 반드시 반영하라.
* 세션 요청사항보다 프로젝트 지침을 우선한다는 정책을 반드시 반영하라.
* 단, 지침 자체를 바꾸라는 명시적 요청은 Governance Change로 분리하라.
