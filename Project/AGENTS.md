# AGENTS.md — 프로젝트 진입 지침

이 문서는 프로젝트의 에이전트 진입점이다.
세부 규칙을 모두 담지 않고, **작업 유형과 경로에 따라 필요한 문서로 라우팅**한다.

> 이 문서는 "무엇을 어디서 읽고, 어떤 순서로 따를지"만 정한다.
> 실제 규칙·상태·절차·결정은 각각 ProjectRules / ProjectState / Playbooks / Decisions에 있다.

---

## 1. 문서 체계 한눈에 보기

| 위치 | 책임 | 변경 빈도 |
| --- | --- | --- |
| `Docs/ProjectRules/` | 안정적인 최소 전역 규칙 | 낮음 |
| `Docs/ProjectState/` | 현재 마일스톤·스프린트·이슈 등 가변 상태 | 높음 |
| `Docs/Playbooks/` | 범용 작업 유형별 절차서 | 중간 |
| `Docs/Decisions/` | ADR 원문 저장소 | 낮음 |
| `Docs/Governance/` | 지침 변경 절차 | 낮음 |
| `Docs/Validation/` | 검증 기준 문서 | 낮음 |
| `Docs/WorkLogs/` | 작업 결과 기록 | 영향도 따라 |
| `Docs/Templates/` | 디렉토리 로컬 문서 원본 템플릿 | 낮음 |
| `Tools/` | 선택 검증 도구(자동 실행 안 함) | 낮음 |
| `<dir>/CONTEXT.md` | 디렉토리 탐색용 짧은 지도 | 중간 |
| `<dir>/AGENTS.md` | 경로별 강한 로컬 규칙(선택) | 낮음 |
| `<dir>/ADR-Refs.md` | 디렉토리에 영향을 주는 ADR 참조(선택) | 낮음 |

문서 체계 전체 인덱스는 `Docs/README.md`를 참고한다.

---

## 2. 지침 우선순위

충돌이 발생하면 아래 순서로 상위 항목이 우선한다.

```text
1. Safety / Tool / Platform Constraints   # 안전·도구·플랫폼 제약
2. Project Entry Instructions             # 이 AGENTS.md
3. ProjectRules                           # 안정 전역 규칙
4. Directory AGENTS.md                    # 경로별 강한 로컬 규칙
5. Playbooks                              # 안전한 작업 절차
6. ProjectState                           # 현재 우선순위와 상태
7. Directory CONTEXT.md                   # 탐색 지도
8. Session Request                        # 이번 작업 요청
9. Inferred Intent                        # 추론된 의도
```

> `Playbooks`(5)는 `ProjectState`(6)보다 위에 둔다. 현재 상태가 안전한 작업 절차를
> 약화시키지 않도록 하기 위함이다.

---

## 3. 세션 요청 충돌 처리

```text
세션 요청이 프로젝트 지침과 충돌하면 프로젝트 지침을 우선한다.
세션 요청을 그대로 수행하지 않고, 지침을 만족하는 대안을 선택한다.
대안이 불가능하면 충돌 사항을 보고하고 변경을 보류한다.
```

- 충돌 보고 시 어떤 문서의 어떤 규칙과 충돌했는지 경로와 함께 명시한다.
- 로컬 `AGENTS.md`가 상위 지침과 충돌하면 항상 상위 지침을 우선한다.

---

## 4. Governance Change 처리

사용자가 지침, 정책, ADR, Playbook, CONTEXT, 작업 절차 변경을 명시적으로 요청하면
**Governance Change**로 취급한다. 일반 기능 구현 요청보다 신중하게 처리한다.

판단 기준:
- "이 규칙을 바꿔라", "이제부터 X를 기본으로 해라" → Governance Change
- "이 기능을 구현해라", "이 버그를 고쳐라" → 일반 작업 요청

### 대화형 에이전트

```text
1. 변경 대상 문서를 식별한다.
2. 기존 지침과 충돌 여부를 설명한다.
3. 변경안을 제시한다.
4. 사용자 승인을 받은 뒤 문서를 수정한다.
5. 중요한 결정이면 ADR 추가 또는 갱신을 제안한다.
```

### 비대화형 에이전트

```text
1. 기존 지침을 즉시 변경하지 않는다.
2. Docs/Governance/CHANGE-TEMPLATE.md 형식의 변경 제안 문서를 생성한다.
3. 작업 결과에 "승인 필요"라고 명시한다.
4. 사용자가 명시적으로 "바로 수정"을 요청한 경우에만 문서 변경까지 수행한다.
```

상세 기준은 `Docs/Governance/README.md`를 따른다.

---

## 5. 작업 유형별 라우팅

작업을 시작하기 전에 해당 작업 유형의 Playbook과 관련 ProjectRules를 읽는다.
Playbook 목록과 형식은 `Docs/Playbooks/README.md`를 참고한다.

| 작업 유형 | Playbook |
| --- | --- |
| 신규 기능 추가 | `Docs/Playbooks/add-new-feature.md` |
| 기존 기능 수정 | `Docs/Playbooks/modify-existing-feature.md` |
| 리팩터링 | `Docs/Playbooks/refactor-code.md` |
| 버그 조사 | `Docs/Playbooks/investigate-bug.md` |
| 크래시 조사 | `Docs/Playbooks/investigate-crash.md` |
| 성능 최적화 | `Docs/Playbooks/optimize-performance.md` |
| 테스트 추가/수정 | `Docs/Playbooks/add-or-update-test.md` |
| 콘텐츠/데이터 갱신 | `Docs/Playbooks/update-content-or-data.md` |
| 빌드/릴리즈 변경 | `Docs/Playbooks/update-build-or-release.md` |
| 문서 갱신 | `Docs/Playbooks/update-documentation.md` |

> UI/로컬라이징/네트워크/저장/플랫폼 빌드 등 특수 영역 절차는 기본 템플릿에 없다.
> 프로젝트에 필요해지면 해당 Playbook과 ProjectRules를 그때 추가한다.

---

## 6. 경로 기반 로컬 문서 탐색

별도 등록표(`DirectoryIndex.md`)는 만들지 않는다. 대신 경로 자체를 컨텍스트 필터로 쓴다.

```text
작업 대상 경로에서 시작해 프로젝트 루트까지 상위 디렉토리를 순회하며 다음 파일을 찾는다.

- AGENTS.md
- CONTEXT.md
- ADR-Refs.md

가장 가까운 파일을 우선하되, 상위 파일도 적용 범위가 겹치면 함께 읽는다.
상위 디렉토리의 로컬 지침은 하위 경로에 재귀적으로 적용된다.
프로젝트 루트의 AGENTS.md는 항상 적용된다.
```

---

## 7. 로컬 문서 생성 규칙

로컬 문서는 모든 디렉토리에 만들지 않는다. 유지 비용을 낮추기 위해 선택적으로 만든다.

```text
로컬 CONTEXT.md는 해당 디렉토리 구조를 이해하는 데 반복적으로 도움이 될 때만 생성한다.
로컬 AGENTS.md는 상위 규칙과 다른 강한 로컬 규칙이 있을 때만 생성한다.
ADR-Refs.md는 관련 ADR이 실제로 존재할 때만 생성한다.
새 로컬 문서가 필요하면 Docs/Templates/에서 복사해 사용한다.
```

`Source/`·`Assets/` 같은 디렉토리는 프로젝트 기술 기반에 따라 없을 수 있으므로 고정하지 않는다.

---

## 8. 작업 완료 보고 형식

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

영향도가 큰 작업은 동일 내용을 `Docs/WorkLogs/`에 기록한다(판단 기준: `Docs/WorkLogs/README.md`).

---

## 9. 문서 갱신 의무

- 동작/구조가 바뀌면 영향받는 `CONTEXT.md`를 갱신한다. 로컬 문서가 아직 없고 위 7절 기준에 해당하면 `Docs/Templates/`에서 복사해 만든다.
- 현재 상태(마일스톤·이슈·기술부채 등)가 바뀌면 `Docs/ProjectState/`를 갱신한다.
- 새 구조적 결정을 내렸으면 `Docs/Decisions/`에 ADR을 추가하고, 영향 디렉토리에 ADR이 실제로 영향을 주면 `ADR-Refs.md`에 참조를 추가한다.
- ADR을 폐기/대체했거나 기능을 제거했으면 그 시점에 영향 경로의 `ADR-Refs.md`에서 해당 참조를 제거하고 `CONTEXT.md`를 정리한다(원문은 `Docs/Decisions/`에 보존).

---

## 10. ADR 참조 방식

- ADR **원문**은 모두 `Docs/Decisions/`에만 둔다.
- 각 디렉토리에는 원문을 복사하지 않고 `ADR-Refs.md`에 **링크와 영향 요약**만 둔다.
- 하나의 ADR이 여러 영역에 영향을 주면 각 영역의 `ADR-Refs.md`에 참조를 추가한다.

---

## 11. 검증 스크립트 실행 정책

```text
/Tools의 검증 스크립트는 선택 도구다.
일반 작업 완료 루틴에서 자동 실행하지 않는다.
사용자 요청, 프로젝트 지침, CI 설정, 검증 담당자 지시가 있을 때만 실행한다.
스크립트를 실행하지 않았더라도 작업 완료 보고의 검증 결과에는 수행한 수동/논리 검증을 작성한다.
스크립트 실행 실패는 작업 실패가 아니라 별도 검증 이슈로 보고한다.
```

검증 기준은 `Docs/Validation/README.md`, 수동 점검은 `Docs/Validation/manual-checklist.md`를 따른다.

---

## 12. 문서 수명·예산 관리 (성숙기 병목 방지)

프로젝트가 성숙하면 **매 작업 항상 읽히는 세로 경로**(루트 `AGENTS.md` → 잎 디렉토리의
`CONTEXT.md` / 로컬 `AGENTS.md` / `ADR-Refs.md`)가 비대해져 병목이 된다.
목표는 이 경로의 총량을 **프로젝트 나이와 무관하게 평평하게 유지**하는 것이다.

```text
1. 압축이 아니라 상태로 관리한다.
   ADR 원문(Decisions/)은 보존(append-only)하고, 폐기는 Status로 표시한다.
   ADR-Refs.md에는 현재 구속력 있는(Active) 참조만 남긴다.
2. 항상 읽히는 문서에 크기 예산을 둔다.
   예산 초과는 문서를 늘릴 신호가 아니라, 디렉토리 분할·규칙 하위 이동(push-down) 신호다.
3. 규칙·제약은 영향을 받는 가장 좁은 디렉토리에 둔다(push-down).
   루트/상위에 쌓아 모든 작업이 그 비용을 내게 하지 않는다.
4. 정리는 supersede/제거 이벤트 시 즉시 + 마일스톤마다 GC로 한다.
```

상세 기준은 `Docs/ProjectRules/documentation-policy.md`를 따른다.
