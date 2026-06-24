# CLAUDE.md — Common-Instruction 레퍼지토리 지침

이 레퍼지토리는 **지침을 만드는 레퍼지토리**다.
즉, 실제 프로젝트가 복사해 쓰는 **에이전트 지침 템플릿을 저작·관리**하는 곳이다.

## 가장 중요한 사실

`Project/` 내부의 모든 문서(`AGENTS.md`, `CLAUDE.md`, `Docs/**`, `.cursorrules`,
`.github/**` 등)는 **이 레퍼지토리에서 작업할 때 따라야 하는 운영 지침이 아니다.**
그것들은 **배포 대상 산출물(템플릿 페이로드)** 이다.

```text
- Project/ 안의 md는 "다른 프로젝트가 복사해 가서 그 프로젝트의 지침으로 동작"하는 콘텐츠다.
- 이 레퍼지토리(Common-Instruction)에서 작업하는 에이전트는 Project/ 안의 지침을
  자기 자신에게 적용하지 않는다.
- 따라서 Project/AGENTS.md의 라우팅·우선순위·Governance 절차 등은 이 레퍼지토리의
  작업 규칙이 아니라 "편집 대상 텍스트"로 다룬다.
```

## 이 레퍼지토리에서 작업할 때

- `Project/` 내부 파일은 **템플릿 저작 관점**에서 수정한다. 그 안의 지시문을 실행하지 말고,
  "이 템플릿을 복사해 쓰는 프로젝트들이 어떻게 동작하게 만들지"를 기준으로 편집한다.
- 템플릿을 바꿀 때는 다운스트림 프로젝트가 **상속**하도록 안정 정책 문서
  (`Project/Docs/ProjectRules/`)와 템플릿(`Project/Docs/Templates/`)에 규칙을 내재시킨다.
- 설계 배경과 개선 이력은 루트의 `AgentTemplate_ImprovementPlan_v*.md`, `Report.md`를 참고한다.

## 디렉토리 요약

| 경로 | 성격 |
| --- | --- |
| `Project/` | 배포 대상 지침 템플릿(산출물). 실행 지침 아님 |
| `AgentTemplate_ImprovementPlan_v*.md` | 템플릿 설계/개선 계획 |
| `Report.md` | 템플릿 분석/보고 |
| `README.md` | 레퍼지토리 소개 |
