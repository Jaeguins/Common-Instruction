# Docs — 지침 문서 인덱스

이 폴더는 프로젝트의 에이전트 지침 문서 루트다.
상세 실행 규칙은 `/AGENTS.md`를 따른다. 이 문서는 라우팅용 최소 인덱스다.

## 하위 폴더 책임

| 폴더 | 책임 |
| --- | --- |
| `ProjectRules/` | 최소 전역 규칙 (안정) |
| `ProjectState/` | 현재 마일스톤·상태 (가변) |
| `Playbooks/` | 범용 작업 유형별 절차 |
| `Decisions/` | ADR 원문 저장소 |
| `Governance/` | 지침 변경 절차 |
| `Validation/` | 검증 기준 문서 |
| `WorkLogs/` | 작업 결과 기록 |
| `Templates/` | 디렉토리 로컬 문서 원본 템플릿 |

검증 도구는 `/Tools`에 있다(선택 실행).

## 원칙

- 프로젝트별 규칙·절차(UI/네트워크/저장/플랫폼 등)는 기본 템플릿에 없다. **필요 시 추가**한다.
- 로컬 문서(`CONTEXT.md`/`AGENTS.md`/`ADR-Refs.md`)는 `Templates/`에서 **복사**해 쓴다.
- 로컬 문서는 모든 디렉토리에 만들지 않는다. 생성 기준은 `/AGENTS.md` 참고.
- ADR 원문은 `Decisions/`에만 둔다. 디렉토리에는 `ADR-Refs.md` 참조만 둔다.

## 구조 예시

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
    ProjectState/                            # 현재 프로젝트 상태
    Playbooks/                               # 범용 작업 절차서
    Decisions/                               # ADR 원문 저장소
    Governance/                              # 지침 변경 절차
    Validation/                              # 검증 기준 문서
    WorkLogs/                                # 작업 결과 기록
    Templates/                               # 로컬 문서 원본 템플릿
  Tools/                                     # 선택 검증 도구

  # 아래는 프로젝트 기술 기반에 따라 생길 수 있는 디렉토리 예시다.
  # 고정 폴더가 아니며, 필요 시 Docs/Templates를 복사해 로컬 문서를 둔다.
  <code-dir>/                                # (선택) 코드 디렉토리
    CONTEXT.md                               # 필요 시 Templates에서 복사
  <asset-dir>/                               # (선택) 에셋 디렉토리
    CONTEXT.md                               # 필요 시 Templates에서 복사
```
