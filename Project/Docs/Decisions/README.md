# Decisions — ADR 원문 저장소

이 폴더는 모든 ADR(Architecture Decision Record) **원문**을 모은다.

## ADR 관리 원칙

- ADR 원문은 모두 `/Docs/Decisions`에 둔다.
- 영향을 받는 디렉토리에는 `ADR-Refs.md`로 링크만 둔다.
- ADR 원문을 디렉토리마다 중복 복사하지 않는다.
- 하나의 ADR이 여러 영역에 영향을 주면 각 영역 `ADR-Refs.md`에 참조를 추가한다.
- ADR 파일명은 영향 범위를 포함할 수 있다.

## 수명·폐기 원칙 (압축하지 않는다)

- ADR 원문은 **append-only 감사 로그**다. 지우거나 압축하지 않는다.
- 결정이 무효화되면 원문을 삭제하지 말고 `Status`를 `Deprecated`/`Superseded`로 바꾸고
  후속 ADR을 `Superseded-by`로 가리킨다.
- 폐기 시 영향 경로의 `ADR-Refs.md`에서 해당 링크만 제거한다. **원문은 여기 그대로 둔다.**
- `ADR-Refs.md`에는 현재 구속력 있는(Active) 참조만 남긴다. 자세한 기준은
  `../ProjectRules/documentation-policy.md`의 "ADR 수명 관리"를 따른다.

## 파일명 예시

```text
ADR-DATA-0001-table-memory-layout.md
ADR-UI-0001-screen-navigation.md
ADR-NET-0001-message-versioning.md
ADR-SAVE-0001-save-versioning.md
ADR-PLATFORM-0001-android-build-policy.md
```

## 작성 방법

- 새 결정을 내리면 `ADR-TEMPLATE.md`를 복사해 작성한다.
- 번호는 스코프별 4자리 일련번호를 사용한다.
- 작성 후 영향 디렉토리의 `ADR-Refs.md`에 참조를 추가한다.
- 예시는 `ADR-EXAMPLE-0001.md`를 참고한다.
