# Tools — 선택 검증 도구

이 폴더의 스크립트는 **선택 검증 도구**다.

## 도구 사용 기준

- 일반 에이전트 작업 완료 루틴에서 **자동 실행하지 않는다.**
- 실행은 사용자 요청, CI 설정, 검증 담당자 지시가 있을 때만 수행한다.
- 환경 문제(Python/Node/shell 차이 등)로 실행에 실패하면, 스크립트 결과 대신
  `../Docs/Validation/manual-checklist.md`를 사용한다.
- 스크립트 실행 실패는 작업 실패가 아니라 별도 검증 이슈로 보고한다.

## 포함 도구

- `validate-doc-links.py` — Markdown 상대 링크/참조 경로 존재 점검
  (문서 정리 GC 시 죽은 `ADR-Refs.md` 링크 탐지에 사용)
- `validate-agent-docs.py` — 지침 템플릿 기본 구조 점검
- `validate-doc-budget.py` — 항상 읽히는 문서의 크기 예산(`CONTEXT.md` 줄 수,
  `ADR-Refs.md` 활성 참조 수)과 폐기(Deprecated/Superseded) ADR 잔존 참조 점검
  (기준: `../Docs/ProjectRules/documentation-policy.md`)

## 실행 예시

```bash
python Tools/validate-doc-links.py
python Tools/validate-agent-docs.py
python Tools/validate-doc-budget.py
```

두 스크립트는 표준 라이브러리만 사용한다(추가 의존성 없음).
