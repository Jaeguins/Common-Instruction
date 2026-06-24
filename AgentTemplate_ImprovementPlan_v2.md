# LLM Agent 지침 템플릿 개선 계획안

## 0. 목적

이 문서는 기존 `Project/` 기반 LLM Agent 지침 템플릿의 1차 구현 결과를 바탕으로, 다음 개선 작업을 수행할 에이전트에게 전달할 계획안이다.

핵심 방향은 다음과 같다.

```text
기본 템플릿은 더 작고 범용적으로 유지한다.
프로젝트별 선택 규칙은 기본 템플릿에 넣지 않는다.
로컬 문서는 별도 등록표 없이 경로 규칙으로 탐색한다.
대화형 에이전트와 비대화형 에이전트 모두 동작 가능하게 한다.
검증 도구는 템플릿에 포함하지 않고, 검증 수행 절차만 문서화한다.
인간용 설명 문서는 최소화하고, 에이전트 실행 지침 중심으로 정리한다.
```

---

## 1. 반영할 주요 피드백

### 1.1 Optional 규칙 파일 제거

기존 개선 제안에서는 `ProjectRules/Core`와 `ProjectRules/Optional`을 나누는 방식을 제안했으나, 이번 개선에서는 Optional 규칙 파일을 기본 템플릿에 포함하지 않는다.

이유:

- Optional 파일이 많아지면 사용하지 않는 규칙도 기본 컨텍스트 후보가 된다.
- Unity, Unreal, 모바일, 콘솔, 서버 등 프로젝트별 차이가 커서 범용 템플릿에 포함하면 오히려 노이즈가 된다.
- 필요한 프로젝트에서 필요한 시점에 직접 추가하는 편이 더 안전하다.

따라서 기본 `ProjectRules/`에는 모든 프로젝트에서 거의 공통으로 쓸 수 있는 최소 규칙만 둔다.

### 1.2 로컬 문서 등록표 제거

기존 개선 제안에서는 `Docs/DirectoryIndex.md`를 두고 로컬 문서를 등록하는 방식을 제안했으나, 이번 개선에서는 별도 등록표를 만들지 않는다.

대신 다음 경로 탐색 규칙을 사용한다.

- 에이전트는 현재 작업 대상 파일 또는 디렉토리에서 시작한다.
- 상위 디렉토리로 올라가며 `AGENTS.md`, `CONTEXT.md`, `ADR-Refs.md`를 찾는다.
- 프로젝트 루트를 넘지 않는다.
- 가장 가까운 로컬 문서를 우선한다.
- 상위 로컬 문서도 범위가 겹치면 함께 참조한다.
- 특정 상위 폴더 아래에는 모든 하위 폴더에 동일 규칙이 재귀 적용된다고 본다.

이 방식은 별도 인덱스를 관리하지 않아도 되며, 경로 자체가 컨텍스트 필터로 작동한다.

### 1.3 대화형/비대화형 에이전트 모두 고려

일부 Agent AI 솔루션은 사용자와 대화하며 승인받을 수 있지만, 일부는 한 번의 프롬프트로 파일을 수정하고 종료될 수 있다.

따라서 Governance Change, 지침 충돌, 큰 작업 판단 등은 대화형 플로우만 전제해서는 안 된다.

개선 원칙:

- 대화형 가능: 충돌 또는 지침 변경이 필요하면 사용자에게 확인 요청
- 비대화형: 실제 변경을 보류하고 `Proposed` 상태의 제안 문서를 생성
- 명시적 승인 없이 지침, ADR, 전역 규칙을 임의로 변경하지 않음
- 단, 사용자가 “바로 수정하라”고 명시한 경우에는 승인된 요청으로 간주

### 1.4 큰 작업 기준 일반화 축소

기존 개선 제안에서 “3개 이상 파일 수정” 같은 기준을 제안했으나, 프로젝트마다 큰 작업의 기준이 다를 수 있다.

이번 개선에서는 고정 수치 기준을 제거하고, 큰 작업 여부를 다음처럼 정의한다.

- 변경 영향 범위를 설명해야 할 정도인가
- 되돌리기 어려운 변경인가
- 전역 규칙, 저장 포맷, 네트워크, 빌드, 에셋 파이프라인, 공개 API 등에 영향을 주는가
- 작업자가 후속 맥락 없이 이해하기 어려운가
- 검증 결과 또는 리스크를 남겨야 하는가

즉 “큰 작업”은 수치가 아니라 영향도 기준으로 판단한다.

### 1.5 검증 스크립트는 포함하되 기본 작업 루틴에서는 제외

기존 개선 제안에서는 링크 검증 스크립트 추가를 제안했고, 이후에는 환경 차이를 고려해 스크립트 미포함을 검토했다.

이번 개선에서는 검증 스크립트를 템플릿에 포함하되, 일반 에이전트 작업 완료 루틴에는 포함하지 않는다.

이유:

- 검증 스크립트 자체는 프로젝트 템플릿의 품질 관리에 도움이 된다.
- 다만 사용자 환경에 따라 Python, Node, shell, CI 환경이 다를 수 있다.
- 모든 일반 작업마다 스크립트 실행을 강제하면 에이전트 실패 원인이 늘어난다.
- 검증 실행 여부는 사람 작업자, CI 담당자, 또는 프로젝트별 자동화 담당자가 결정하는 편이 낫다.

따라서 다음 원칙을 적용한다.

```text
검증 스크립트는 Project/Tools/에 제공한다.
에이전트의 기본 작업 완료 루틴에는 스크립트 실행을 넣지 않는다.
필요 시 사용자 또는 프로젝트 지침이 명시적으로 요청한 경우에만 실행한다.
스크립트 실행 실패는 작업 실패가 아니라 별도 검증 이슈로 보고한다.
```

검증 관련 문서는 다음 위치에 둔다.

```text
Docs/Validation/
  README.md
  manual-checklist.md

Tools/
  README.md
  validate-doc-links.py
  validate-agent-docs.py
```

### 1.6 AI 작업에서 “빠른 임시 구현 우선” 제거

AI에게 “빠른 임시 구현 우선”이라는 상태 지시는 의미가 약하다.

원칙:

- AI는 가능한 한 견고하고 정확한 구현안을 빠르게 제안해야 한다.
- 임시 구현 여부는 작업자의 판단과 프로젝트 상황에 따른다.
- `ProjectState`는 안정 절차를 약화시키는 지시를 담지 않는다.
- `ProjectState`는 우선순위, 현재 제약, 진행 상황, 열려 있는 질문만 기록한다.

따라서 지침 우선순위에서 `Playbooks`는 `ProjectState`보다 위에 둔다.

### 1.7 현재 위치에 따른 문서 변화 최소화

경로별 문서를 둘 수는 있지만, 현재 위치마다 문서 내용이 크게 달라지면 유지 비용이 커진다.

개선 원칙:

- 로컬 `AGENTS.md`는 가급적 생성하지 않는다.
- 대부분의 디렉토리는 `CONTEXT.md`만 둔다.
- 로컬 `AGENTS.md`는 상위 규칙과 다른 “강한 로컬 규칙”이 있을 때만 둔다.
- `ADR-Refs.md`는 관련 ADR이 실제로 있을 때만 둔다.
- `CONTEXT.md`는 현재 디렉토리와 바로 하위 디렉토리까지만 설명한다.
- 반복 가능한 템플릿 구조를 유지하고, 문서별 개성은 최소화한다.

### 1.8 인간용 문서 최소화

이번 템플릿은 인간용 설명서가 아니라 에이전트 실행 지침 템플릿이다.

따라서 `Docs/README.md`는 사람을 위한 긴 설명서가 아니라, 에이전트가 문서 체계를 이해하고 라우팅하는 데 필요한 최소 인덱스로 둔다.

---

## 2. 개선 후 목표 구조

아래 구조로 기존 `Project/` 템플릿을 개선한다.

```text
Project/                                      # 프로젝트 템플릿 루트
  AGENTS.md                                  # 에이전트 진입점
  CLAUDE.md                                  # Claude 위임 지침
  .cursorrules                               # Cursor 위임 지침
  .github/                                   # GitHub 설정
    copilot-instructions.md                  # Copilot 위임 지침
    pull_request_template.md                 # PR 보고 형식

  Docs/                                      # 지침 문서 루트
    README.md                                # 문서 체계 인덱스

    ProjectRules/                            # 최소 전역 규칙
      README.md                              # 규칙 추가 기준
      coding-convention.md                   # 코드 스타일 기준
      architecture-policy.md                 # 구조 설계 기준
      testing-policy.md                      # 테스트 기준
      performance-policy.md                  # 성능 판단 기준
      documentation-policy.md                # 문서 갱신 기준

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
      add-new-feature.md                     # 신규 기능 절차
      modify-existing-feature.md             # 기존 기능 수정
      refactor-code.md                       # 리팩터링 절차
      investigate-bug.md                     # 버그 조사 절차
      investigate-crash.md                   # 크래시 조사
      optimize-performance.md                # 성능 최적화
      add-or-update-test.md                  # 테스트 추가/수정
      update-content-or-data.md              # 콘텐츠/데이터 갱신
      update-build-or-release.md             # 빌드/릴리즈 변경
      update-documentation.md                # 문서 갱신 절차

    Decisions/                               # ADR 원문 저장소
      README.md                              # ADR 운영 기준
      ADR-TEMPLATE.md                        # ADR 템플릿
      ADR-EXAMPLE-0001.md                    # ADR 예시

    Governance/                              # 지침 변경 절차
      README.md                              # 변경 처리 기준
      CHANGE-TEMPLATE.md                     # 변경 제안 템플릿

    Validation/                              # 검증 기준 문서
      README.md                              # 검증 운영 기준
      manual-checklist.md                    # 수동 점검 항목

    WorkLogs/                                # 작업 결과 기록
      README.md                              # 작업 로그 기준
      WORKLOG-TEMPLATE.md                    # 작업 로그 템플릿

    Templates/                               # 로컬 문서 템플릿
      README.md                              # 복사 사용법
      CONTEXT.md                             # 디렉토리 지도 원본
      AGENTS.md                              # 로컬 지침 원본
      ADR-Refs.md                            # ADR 참조 원본

  Tools/                                     # 선택 검증 도구
    README.md                                # 도구 사용 기준
    validate-doc-links.py                    # 링크 점검 스크립트
    validate-agent-docs.py                   # 지침 구조 점검
```

---

## 3. 삭제 또는 축소할 파일

기존 템플릿에서 다음 파일은 기본 생성 대상에서 제거한다.

```text
Docs/ProjectRules/ui-policy.md
Docs/ProjectRules/localization-policy.md
Docs/ProjectRules/data-table-policy.md
Docs/ProjectRules/save-data-policy.md
Docs/ProjectRules/network-policy.md
Docs/ProjectRules/asset-pipeline-policy.md
Docs/ProjectRules/addressables-policy.md
Docs/ProjectRules/platform-android-policy.md
Docs/ProjectRules/platform-ios-policy.md

Docs/Playbooks/add-new-ui-screen.md
Docs/Playbooks/add-new-localized-text.md
Docs/Playbooks/add-new-data-table.md
Docs/Playbooks/add-new-editor-tool.md
Docs/Playbooks/add-new-network-message.md
Docs/Playbooks/add-new-save-field.md
Docs/Playbooks/fix-platform-build-error.md
Docs/Playbooks/update-bundled-content.md
```

삭제 이유:

- 특정 엔진, 플랫폼, 장르, 시스템을 암묵적으로 전제한다.
- 범용 템플릿의 기본 컨텍스트 후보를 과도하게 늘린다.
- 프로젝트별 필요가 생겼을 때 추가하는 편이 더 안전하다.

단, `ProjectRules/README.md`와 `Playbooks/README.md`에는 다음 원칙을 명시한다.

```text
프로젝트에 UI, 로컬라이징, 네트워크, 저장, 데이터테이블, 플랫폼별 빌드, 에셋 번들 등 특수 영역이 생기면 해당 규칙 문서와 플레이북을 그때 추가한다.
기본 템플릿은 해당 영역을 미리 생성하지 않는다.
```

---

## 4. `AGENTS.md` 개선 계획

`Project/AGENTS.md`는 가장 중요한 실행 지침이다.

다음 내용을 반영한다.

### 4.1 역할

```text
이 문서는 프로젝트의 에이전트 진입점이다.
세부 규칙을 모두 담지 않고, 작업 유형과 경로에 따라 필요한 문서로 라우팅한다.
```

### 4.2 지침 우선순위

`ProjectState`보다 `Playbooks`를 위에 둔다.

```text
1. Safety / Tool / Platform Constraints
2. Project Entry Instructions
3. ProjectRules
4. Directory AGENTS.md
5. Playbooks
6. ProjectState
7. Directory CONTEXT.md
8. Session Request
9. Inferred Intent
```

해석:

- `ProjectRules`: 안정 전역 규칙
- `Directory AGENTS.md`: 경로별 강한 로컬 규칙
- `Playbooks`: 안전한 작업 절차
- `ProjectState`: 현재 우선순위와 상태
- `Directory CONTEXT.md`: 탐색 지도
- `Session Request`: 이번 작업 요청

### 4.3 세션 요청 충돌 처리

```text
세션 요청이 프로젝트 지침과 충돌하면 프로젝트 지침을 우선한다.
세션 요청을 그대로 수행하지 않고, 지침을 만족하는 대안을 선택한다.
대안이 불가능하면 충돌 사항을 보고하고 변경을 보류한다.
```

### 4.4 Governance Change 처리

대화형/비대화형 모두 대응한다.

```text
사용자가 지침, 정책, ADR, Playbook, CONTEXT, 작업 절차 변경을 명시적으로 요청하면 Governance Change로 취급한다.
```

#### 대화형 에이전트

```text
1. 변경 대상 문서를 식별한다.
2. 기존 지침과 충돌 여부를 설명한다.
3. 변경안을 제시한다.
4. 사용자 승인을 받은 뒤 문서를 수정한다.
5. 중요한 결정이면 ADR 추가 또는 갱신을 제안한다.
```

#### 비대화형 에이전트

```text
1. 기존 지침을 즉시 변경하지 않는다.
2. Docs/Governance/CHANGE-TEMPLATE.md 형식의 변경 제안 문서를 생성한다.
3. 작업 결과에 “승인 필요”라고 명시한다.
4. 사용자가 명시적으로 “바로 수정”을 요청한 경우에만 문서 변경까지 수행한다.
```

### 4.5 경로 기반 로컬 문서 탐색 규칙

`DirectoryIndex.md`는 만들지 않는다.

대신 다음 규칙을 `AGENTS.md`에 포함한다.

```text
작업 대상 경로에서 시작해 프로젝트 루트까지 상위 디렉토리를 순회하며 다음 파일을 찾는다.

- AGENTS.md
- CONTEXT.md
- ADR-Refs.md

가장 가까운 파일을 우선하되, 상위 파일도 적용 범위가 겹치면 함께 읽는다.
상위 디렉토리의 로컬 지침은 하위 경로에 재귀적으로 적용된다.
프로젝트 루트의 AGENTS.md는 항상 적용된다.
```

### 4.6 로컬 문서 생성 규칙

```text
로컬 CONTEXT.md는 해당 디렉토리의 구조를 이해하는 데 반복적으로 도움이 될 때만 생성한다.
로컬 AGENTS.md는 상위 규칙과 다른 강한 로컬 규칙이 있을 때만 생성한다.
ADR-Refs.md는 관련 ADR이 실제로 존재할 때만 생성한다.
새 로컬 문서가 필요하면 Docs/Templates/에서 복사해 사용한다.
```

### 4.7 작업 완료 보고 형식

기존 8항목은 유지한다.

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

### 4.8 검증 스크립트 실행 정책

다음을 `AGENTS.md`에 명시한다.

```text
/Tools의 검증 스크립트는 선택 도구다.
일반 작업 완료 루틴에서 자동 실행하지 않는다.
사용자 요청, 프로젝트 지침, CI 설정, 검증 담당자 지시가 있을 때만 실행한다.
스크립트를 실행하지 않았더라도 작업 완료 보고의 검증 결과에는 수행한 수동/논리 검증을 작성한다.
```

---

## 5. `Docs/Templates/` 개선 계획

### 5.1 `Docs/Templates/README.md`

다음 내용을 추가한다.

```text
로컬 문서는 프로젝트의 모든 디렉토리에 만들지 않는다.
반복적으로 에이전트가 혼동하는 디렉토리, 책임이 복잡한 디렉토리, ADR 영향을 받는 디렉토리에만 만든다.
```

복사 후 수정 체크리스트:

```text
- 문서 제목을 실제 경로명으로 변경
- Scope를 실제 경로로 변경
- placeholder 제거
- 관련 ProjectRules 연결
- 관련 Playbooks 연결
- 관련 ADR이 있으면 ADR-Refs.md 생성
- 관련 ADR이 없으면 ADR-Refs.md는 만들지 않음
- 상위 CONTEXT.md와 중복 설명 제거
```

### 5.2 `CONTEXT.md`

현재 위치 변화에 따른 문서 변경을 최소화하기 위해 다음 형식으로 단순화한다.

```md
# Directory Context

## Scope

TODO: 이 문서가 설명하는 경로를 작성한다.

## Responsibility

TODO: 이 디렉토리의 책임을 3줄 이내로 작성한다.

## Entry Points

TODO: 에이전트가 먼저 볼 주요 파일/하위 폴더를 작성한다.

## Local Map

TODO: 바로 하위 파일/폴더의 역할만 작성한다.

## External Touchpoints

TODO: 이 디렉토리가 참조하는 외부 시스템을 작성한다.

## Cautions

TODO: 수정 시 주의할 점을 작성한다.

## Validation

TODO: 수정 후 확인할 검증 방법을 작성한다.

## Related Documents

TODO: 관련 ProjectRules, Playbooks, ADR-Refs를 작성한다.
```

규칙:

```text
CONTEXT.md는 현재 디렉토리와 바로 하위 디렉토리까지만 설명한다.
상위 설명을 반복하지 않는다.
코드 내용을 길게 요약하지 않는다.
파일 목록 전체를 만들지 않는다.
```

### 5.3 `AGENTS.md`

로컬 `AGENTS.md`는 선택 생성 문서임을 명시한다.

```md
# Local Agent Rules

## Scope

TODO: 이 로컬 지침이 적용되는 경로를 작성한다.

## Use Only When

이 문서는 상위 규칙과 다른 강한 로컬 규칙이 있을 때만 생성한다.

## Local Rules

TODO: 이 경로에서 반드시 지켜야 할 규칙을 작성한다.

## Required Reading

TODO: 이 경로 작업 전 읽어야 할 문서를 작성한다.

## Conflict Policy

상위 지침과 충돌하면 상위 지침을 우선한다.

## Related ADRs

관련 ADR은 ADR-Refs.md를 확인한다.
```

### 5.4 `ADR-Refs.md`

관련 ADR이 있을 때만 생성한다.

```md
# Related ADRs

ADR 원문은 /Docs/Decisions에 둔다.
이 문서에는 현재 경로에 영향을 주는 ADR 링크와 영향 요약만 작성한다.

- /Docs/Decisions/ADR-SCOPE-0000-title.md
  - 영향 요약:
  - 주의 사항:
```

---

## 6. `Docs/Governance/` 추가 계획

### 6.1 목적

지침 변경 요청을 일반 작업 요청과 분리한다.

### 6.2 `Docs/Governance/README.md`

포함할 내용:

```text
Governance Change는 지침, 정책, ADR, Playbook, 로컬 문서 구조를 바꾸는 요청이다.
일반 기능 구현 요청보다 신중하게 처리한다.
대화형 에이전트는 변경안을 설명하고 승인 후 반영한다.
비대화형 에이전트는 변경 제안 문서를 남기고 반영을 보류한다.
사용자가 명시적으로 바로 수정하라고 한 경우에는 승인된 요청으로 간주한다.
```

### 6.3 `CHANGE-TEMPLATE.md`

```md
# Governance Change Proposal

## Summary

변경 제안 요약을 작성한다.

## Target Documents

변경 대상 문서를 작성한다.

## Current Rule

현재 지침을 작성한다.

## Proposed Change

변경안을 작성한다.

## Reason

변경 이유를 작성한다.

## Impact

영향 범위를 작성한다.

## Risks

리스크를 작성한다.

## Required Follow-ups

후속 문서 갱신 또는 ADR 필요 여부를 작성한다.

## Status

Proposed / Approved / Applied / Rejected
```

---

## 7. `Docs/Validation/` 및 `Tools/` 추가 계획

### 7.1 목적

검증 기준과 검증 도구를 함께 제공하되, 일반 작업 루틴에는 포함하지 않는다.

`Docs/Validation/`은 무엇을 점검해야 하는지 설명한다.
`Tools/`는 선택적으로 사용할 수 있는 검증 스크립트를 제공한다.

### 7.2 운영 원칙

```text
검증 스크립트는 템플릿에 포함한다.
일반 에이전트 작업 완료 루틴에서는 실행하지 않는다.
사용자 요청, 프로젝트 지침, CI 설정, 검증 담당자 지시에 따라 실행한다.
스크립트 실행 실패는 작업 실패로 간주하지 않고 별도 검증 이슈로 보고한다.
```

### 7.3 `Docs/Validation/README.md`

포함할 내용:

```text
이 폴더는 검증 기준을 정의한다.
검증 스크립트는 /Tools에 제공되지만 기본 작업 루틴에는 포함하지 않는다.
검증 실행 여부는 프로젝트별 운영 방식에 따른다.
```

### 7.4 `manual-checklist.md`

기본 점검 항목:

```md
# Manual Validation Checklist

## Structure

- Project/AGENTS.md가 존재하는가
- Docs/ProjectRules/README.md가 존재하는가
- Docs/Templates/README.md가 존재하는가
- Docs/Decisions/ADR-TEMPLATE.md가 존재하는가

## Links

- 문서에 적힌 상대경로가 실제로 존재하는가
- ADR-Refs.md는 /Docs/Decisions 아래 ADR만 참조하는가
- Playbook의 Required Reading 경로가 존재하는가

## Placeholders

- 실제 프로젝트 적용 후 TODO가 의도치 않게 남아 있지 않은가
- 복사한 로컬 문서에 placeholder가 남아 있지 않은가

## Governance

- 지침 변경이 Governance Change로 기록되었는가
- 중요한 결정이 ADR로 남았는가

## Local Documents

- 불필요한 로컬 AGENTS.md가 남발되지 않았는가
- CONTEXT.md가 상위 내용을 반복하지 않는가
- ADR이 없는데 ADR-Refs.md를 만들지는 않았는가
```

### 7.5 `Tools/README.md`

포함할 내용:

```text
이 폴더의 스크립트는 선택 검증 도구다.
일반 에이전트 작업 완료 루틴에서 자동 실행하지 않는다.
실행은 사용자 요청, CI 설정, 검증 담당자 지시에 따를 때만 수행한다.
환경 문제로 실행에 실패하면 스크립트 결과 대신 수동 체크리스트를 사용한다.
```

### 7.6 `validate-doc-links.py`

제공 목적:

```text
Markdown 문서의 상대 링크와 참조 경로가 실제로 존재하는지 점검한다.
```

점검 대상 예시:

```text
- Markdown 상대 링크 존재 여부
- AGENTS.md에 언급된 주요 문서 경로 존재 여부
- ADR-Refs.md가 /Docs/Decisions 아래 ADR을 참조하는지
- Playbook의 Required Reading 경로 존재 여부
```

### 7.7 `validate-agent-docs.py`

제공 목적:

```text
에이전트 지침 템플릿의 기본 구조가 유지되고 있는지 점검한다.
```

점검 대상 예시:

```text
- Project/AGENTS.md 존재 여부
- Docs/ProjectRules/README.md 존재 여부
- Docs/Templates/README.md 존재 여부
- Docs/Decisions/ADR-TEMPLATE.md 존재 여부
- Docs/Governance/CHANGE-TEMPLATE.md 존재 여부
- Docs/Validation/manual-checklist.md 존재 여부
```

---

## 8. `Docs/WorkLogs/` 개선 계획

### 8.1 큰 작업 기준을 영향도 중심으로 변경

수치 기준을 사용하지 않는다.

`Docs/WorkLogs/README.md`에 다음을 작성한다.

```text
WorkLog는 모든 작업에 반드시 남기지 않는다.
다만 다음에 해당하면 남기는 것을 권장한다.

- 변경 이유와 결과를 후속 작업자가 알아야 하는 경우
- 되돌리기 어렵거나 영향 범위가 넓은 경우
- 전역 규칙, Playbook, ADR, CONTEXT가 갱신된 경우
- 검증 결과나 리스크를 명시해야 하는 경우
- 임시 우회 또는 기술부채가 추가된 경우
```

파일명 규칙:

```text
YYYY-MM-DD-short-topic.md
YYYY-MM-DD-001-short-topic.md
```

단, 프로젝트별로 다른 명명 규칙이 있으면 `Docs/WorkLogs/README.md`에서 변경할 수 있다고 명시한다.

---

## 9. `Docs/README.md` 개선 계획

인간용 긴 설명서를 제거하고, 에이전트용 최소 인덱스로 축소한다.

포함할 내용:

```text
- 이 폴더가 지침 문서 루트라는 설명
- 각 하위 폴더의 책임
- 프로젝트별 규칙은 필요 시 추가한다는 원칙
- 로컬 문서는 Docs/Templates에서 복사한다는 원칙
- 상세 실행 규칙은 /AGENTS.md를 따른다는 안내
```

넣지 않을 내용:

```text
- 장문의 철학 설명
- 사람을 위한 튜토리얼
- 중복된 우선순위 설명
- AGENTS.md와 겹치는 세부 라우팅
```

---

## 10. 최종 작업 지시 요약

다음 에이전트는 기존 `Project/` 템플릿을 아래 기준으로 수정한다.

```text
1. Optional 성격의 ProjectRules와 Playbooks를 기본 템플릿에서 제거한다.
2. 범용 Core ProjectRules만 남긴다.
3. Playbooks는 특정 시스템명이 아닌 범용 작업 유형 중심으로 재구성한다.
4. DirectoryIndex.md는 만들지 않는다.
5. 경로 기반 상위 탐색 규칙을 AGENTS.md에 명시한다.
6. ProjectState보다 Playbooks를 우선순위 위에 둔다.
7. Governance Change는 대화형/비대화형 플로우를 모두 지원한다.
8. Docs/Governance/를 추가한다.
9. 검증 스크립트는 Tools/에 포함하되 기본 작업 루틴에서는 실행하지 않는다.
10. 로컬 문서는 Docs/Templates에서 선택 복사하는 방식으로 유지한다.
11. 로컬 AGENTS.md와 ADR-Refs.md는 필요할 때만 만든다고 명시한다.
12. CONTEXT.md는 현재 디렉토리와 바로 하위 구조까지만 설명하도록 단순화한다.
13. WorkLogs 생성 기준은 수치가 아니라 영향도 기준으로 작성한다.
14. Docs/README.md는 인간용 설명서가 아니라 최소 인덱스로 축소한다.
15. 모든 문서는 한국어로 작성한다.
```

---

## 11. 기대 결과

개선 후 템플릿은 다음 성격을 갖는다.

```text
- 프로젝트 독립성이 높다.
- 엔진/플랫폼 전제가 줄어든다.
- 기본 문서 수가 줄어든다.
- 로컬 문서 관리 부담이 줄어든다.
- 에이전트가 경로 기반으로 컨텍스트를 찾을 수 있다.
- 지침 변경 요청과 일반 작업 요청이 분리된다.
- 대화형/비대화형 에이전트 모두 적용 가능하다.
- 검증 도구는 포함하되 실행 여부는 프로젝트별로 맡긴다.
```
