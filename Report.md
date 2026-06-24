# 인계 보고서 (Report.md)

> 대상: 오케스트레이션 에이전트 (이후 작업을 지휘·분배하는 상위 에이전트)
> 목적: `Project/` 템플릿의 **현재 상태**, 설계 규칙, 검증 결과, 남은 작업을 인계한다.
> 범위: 이 보고서는 최신 상태(개선 계획 v2 반영 후)를 기준으로 한다. 과거 1차 산출물은 다루지 않는다.

---

## 1. 한 줄 요약

`Project/`는 **엔진/플랫폼 비종속, 대화형/비대화형 에이전트 겸용**의 범용 LLM 에이전트 지침 템플릿이다.
루트 `Project/AGENTS.md`가 단일 진입점(라우터)이며, 세부는 `Docs/` 하위로 라우팅된다. 현재 48개 파일.

---

## 2. 오케스트레이터가 알아야 할 핵심 동작 규칙

이 템플릿을 따르는 하위 에이전트에게 작업을 분배할 때 전제되는 규칙이다.

1. **진입점 고정**: 모든 작업은 `Project/AGENTS.md`를 먼저 읽는 것에서 시작한다. `CLAUDE.md`·`.cursorrules`·`.github/copilot-instructions.md`는 모두 `AGENTS.md`로 위임만 한다.
2. **지침 우선순위** (상위가 우선):
   `Safety/Tool/Platform → Project Entry(AGENTS.md) → ProjectRules → Directory AGENTS.md → Playbooks → ProjectState → Directory CONTEXT.md → Session Request → Inferred Intent`
   - 핵심: **세션 요청은 프로젝트 지침보다 아래**다. 충돌 시 지침을 따르고 보고한다.
   - **Playbooks가 ProjectState보다 위**다(현재 상태가 안전 절차를 약화시키지 않게).
3. **경로 기반 컨텍스트 탐색**: 별도 인덱스(`DirectoryIndex.md`) 없음. 작업 경로에서 루트까지 상위 디렉토리를 순회하며 `AGENTS.md`/`CONTEXT.md`/`ADR-Refs.md`를 찾고, 가까운 것을 우선하되 상위도 함께 적용한다.
4. **Governance Change 분리**: 지침/정책/ADR/Playbook/절차 변경 요청은 일반 작업과 분리.
   - 대화형: 변경안 제시 → 승인 → 반영.
   - 비대화형: `Docs/Governance/CHANGE-TEMPLATE.md` 제안 문서 생성 후 **보류**("승인 필요" 명시). 단 "바로 수정" 명시 시 즉시 반영.
5. **검증 도구는 비자동**: `Tools/`의 스크립트는 기본 작업 루틴에서 자동 실행하지 않는다. 사용자/CI/검증 담당자 지시가 있을 때만. 실행 실패는 작업 실패가 아니라 별도 검증 이슈.
6. **로컬 문서는 선택 생성**: 모든 디렉토리에 만들지 않음. `CONTEXT.md`는 도움이 될 때만, `AGENTS.md`는 강한 로컬 규칙이 있을 때만, `ADR-Refs.md`는 관련 ADR이 실제로 있을 때만. 생성 시 `Docs/Templates/`에서 복사.
7. **작업 완료 보고 8항목**: 변경요약/수정파일/동작변경/검증결과/지침충돌/리스크/후속작업/갱신문서.
8. **영향도 기준 WorkLog**: 모든 작업에 남기지 않고, 되돌리기 어렵거나 영향 범위가 넓거나 규칙/ADR이 갱신될 때 권장.

---

## 3. 현재 파일 구조 (48개)

```text
Project/
  AGENTS.md                                  # 에이전트 진입점(라우터)
  CLAUDE.md                                  # Claude 위임
  .cursorrules                               # Cursor 위임
  .github/
    copilot-instructions.md                  # Copilot 위임
    pull_request_template.md                 # PR 보고 형식(8항목)
  Docs/
    README.md                                # 최소 인덱스
    ProjectRules/                            # 최소 전역 규칙 (Core 5 + README)
      README.md
      coding-convention.md
      architecture-policy.md
      testing-policy.md
      performance-policy.md
      documentation-policy.md
    ProjectState/                            # 가변 상태 (README + 8)
      README.md
      milestone-current.md
      sprint-current.md
      feature-current.md
      known-issues.md
      tech-debt.md
      temporary-workarounds.md
      qa-focus.md
      build-status.md
    Playbooks/                               # 범용 작업 절차 (README + 10)
      README.md
      add-new-feature.md
      modify-existing-feature.md
      refactor-code.md
      investigate-bug.md
      investigate-crash.md
      optimize-performance.md
      add-or-update-test.md
      update-content-or-data.md
      update-build-or-release.md
      update-documentation.md
    Decisions/                               # ADR 원문 저장소
      README.md
      ADR-TEMPLATE.md
      ADR-EXAMPLE-0001.md
    Governance/                              # 지침 변경 절차
      README.md
      CHANGE-TEMPLATE.md
    Validation/                              # 검증 기준
      README.md
      manual-checklist.md
    WorkLogs/                                # 작업 결과 기록
      README.md
      WORKLOG-TEMPLATE.md
    Templates/                               # 로컬 문서 원본 템플릿
      README.md
      CONTEXT.md
      AGENTS.md
      ADR-Refs.md
  Tools/                                     # 선택 검증 도구(비자동)
    README.md
    validate-doc-links.py
    validate-agent-docs.py
```

> `Source/`·`Assets/` 같은 코드/에셋 디렉토리는 **고정 폴더가 아니다.** 프로젝트 기술 기반에 따라
> 생길 때 `Docs/Templates/`에서 로컬 문서를 복사해 둔다.

---

## 4. 각 영역의 책임 (라우팅 기준)

| 영역 | 책임 | 오케스트레이터 활용 |
| --- | --- | --- |
| `ProjectRules/` | 안정 전역 규칙(최소 Core만) | 작업 유형별로 관련 규칙을 하위 에이전트에 함께 전달 |
| `ProjectState/` | 현재 마일스톤·이슈·부채 등 | 작업 분배 전 현재 제약/우선순위 확인 |
| `Playbooks/` | 10개 범용 작업 절차 | 작업 유형 → Playbook 1:1 매핑(§5 AGENTS.md 표) |
| `Decisions/` | ADR 원문(단일 소스) | 되돌리면 안 되는 결정 확인 |
| `Governance/` | 지침 변경 절차 | "규칙 바꿔라" 류 요청을 일반 작업과 분리 |
| `Validation/` | 검증 기준·수동 체크리스트 | 산출물 품질 점검 기준 |
| `WorkLogs/` | 영향도 큰 작업 기록 | 후속 작업자 인계 |
| `Templates/` | 로컬 문서 원본 | 새 디렉토리 문서 생성 시 복사원 |
| `Tools/` | 검증 스크립트(선택) | 명시 요청 시에만 실행 |

작업 유형 ↔ Playbook 매핑(10종): 신규기능 / 기존기능수정 / 리팩터링 / 버그조사 / 크래시조사 / 성능최적화 / 테스트 / 콘텐츠·데이터 / 빌드·릴리즈 / 문서갱신.

---

## 5. 검증 결과 (현재)

- `python Project/Tools/validate-agent-docs.py` → **exit 0** (필수 8파일 누락 0)
- `python Project/Tools/validate-doc-links.py` → **exit 0** (깨진 링크 0)
- 두 스크립트는 표준 라이브러리만 사용(추가 의존성 없음). 스크립트 위치 기준으로 `Project/` 루트를 자동 탐지.
- 모든 placeholder는 의도된 미완성 상태(TODO). 링크 검사기는 placeholder와 `Docs/Templates/`를 제외한다.

---

## 6. 설계상 비종속/범용성 보장 장치

오케스트레이터가 다른 장르/엔진 프로젝트에 이 템플릿을 적용할 때 신뢰할 수 있는 근거:

- ProjectRules는 UI/로컬라이징/네트워크/저장/데이터테이블/플랫폼/번들 같은 **특수 영역을 기본 포함하지 않는다.** 필요 시 추가하라고 `ProjectRules/README.md`·`Playbooks/README.md`에 명시.
- Playbooks는 시스템명이 아닌 **작업 유형** 기준.
- 실제 프로젝트 고유 내용은 어디에도 확정 기재하지 않음(전부 placeholder/TODO).
- 한국어 문서 기준.

---

## 7. 알려진 제약 / 다음 개선 후보 (오케스트레이터 판단용)

강제 사항이 아니라, 다음 라운드에서 분배 가능한 작업 후보다.

1. **링크 검사 범위 한계**: `validate-doc-links.py`는 마크다운 `[text](path)` 문법만 검사한다. 현재 문서는 백틱 경로(`` `../x.md` ``) 위주라 실제 검사된 링크 수가 0이다. → 백틱 경로 파싱 추가 시 실효성↑.
2. **Tools 스크립트 콘솔 인코딩**: Windows 콘솔에서 한글 출력이 깨져 보인다(동작·exit code는 정상). → `PYTHONUTF8=1` 안내 또는 영어 메시지 병기 검토.
3. **Governance 승인 기록 위치**: 비대화형 제안 문서(`CHANGE-TEMPLATE`)의 보관 경로·승인 후 ADR 승격 흐름이 문서로 더 명확해질 수 있다.
4. **ProjectState ↔ Playbooks 우선순위 역전 영향**: 우선순위에서 Playbooks를 위로 올렸으므로, ProjectState의 "긴급 우회 지시"가 절차를 못 누른다. 이 정책이 실제 운영 의도와 맞는지 확인 필요.
5. **로컬 문서 예시 부재**: 현재 `Source/`·`Assets/` 실제 예시 디렉토리가 없다(의도된 설계). 신규 사용자가 복사 워크플로우를 헷갈릴 경우, 채워진 예시 1개를 별도 `examples/`로 제공하는 방안 검토.

---

## 8. 변경 이력 컨텍스트

- 이 템플릿은 두 단계를 거쳤다: (1) `Plan.md` 기반 초기 생성, (2) `AgentTemplate_ImprovementPlan_v2.md` 기반 범용화 개선.
- v2에서 엔진/플랫폼 종속 ProjectRules 9개·Playbooks 8개 제거, Playbooks를 범용 10종으로 재구성, `Governance/`·`Validation/`·`Tools/` 신설, 우선순위에서 Playbooks를 ProjectState 위로 이동, Docs/README를 최소 인덱스화.
- 참고 문서: 리포지토리 루트의 `Plan.md`, `AgentTemplate_ImprovementPlan_v2.md`.

---

## 9. 인계 포인트

- 새 프로젝트 적용: `Project/`를 복사 → ProjectState/ProjectRules의 TODO를 채움 → 특수 영역이 생기면 ProjectRules/Playbooks를 추가.
- 하위 에이전트 분배 시: 작업 유형에 맞는 Playbook + 관련 ProjectRules + 현재 ProjectState를 함께 전달하고, 완료 시 8항목 보고를 받는다.
- 다음 개선은 7절을 우선 검토 대상으로 삼는다.
