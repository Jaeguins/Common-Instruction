# Documentation Policy — 문서 갱신 기준

## Purpose

코드/구조/상태 변경 시 어떤 문서를 어떤 기준으로 갱신해야 하는지 규칙을 담당한다.

## Stable Rules

<!-- TODO: 해당 프로젝트에서 사용하는 방식을 여기에 작성한다. -->
- 동작/구조가 바뀌면 영향받는 `CONTEXT.md`를 갱신한다.
- 현재 상태가 바뀌면 `ProjectState/`의 해당 문서를 갱신한다.
- 구조적 결정은 `Decisions/`에 ADR로 남기고, 영향 경로의 `ADR-Refs.md`에 참조를 추가한다.
- 영향도가 큰 작업은 `WorkLogs/`에 기록한다(판단 기준은 `../WorkLogs/README.md`).
- 인간용 장문 설명 대신 에이전트가 라우팅할 수 있는 최소 정보로 작성한다.

## 항상 읽히는 문서의 수명·예산 (성숙기 병목 방지)

작업 경로를 따라 **매 작업 항상 읽히는 세로 경로 문서**(루트 `AGENTS.md` → 잎 디렉토리의
`CONTEXT.md` / 로컬 `AGENTS.md` / `ADR-Refs.md`)는 프로젝트가 성숙할수록 비대해져 병목이 된다.
목표는 **이 경로의 총량을 프로젝트 나이와 무관하게 평평하게 유지**하는 것이다.

- **현재 유효한 최소 정보만 담는다.** 역사·폐기된 내용·완료된 작업 설명은 담지 않는다.
- **크기 예산을 둔다.** 권장 상한: `CONTEXT.md` ≤ 약 40줄, `ADR-Refs.md` 활성 참조 ≤ 약 15개,
  로컬 `AGENTS.md`는 상위와 다른 강한 규칙만.
- **예산 초과는 문서를 늘릴 신호가 아니라 구조 신호다.** 디렉토리를 분할하거나 규칙을
  더 좁은 하위 디렉토리로 내린다(push-down).
- **push-down 원칙:** 규칙·제약은 영향을 받는 가장 좁은 디렉토리에 둔다. 루트/상위에 쌓아
  모든 작업이 그 비용을 내게 하지 않는다.

## ADR 수명 관리 (압축하지 않는다)

- **ADR 원문(`Decisions/`)은 지우거나 압축하지 않는다.** ADR은 "왜"를 보존하는 감사 로그이며
  append-only로 다룬다. 원문은 기본적으로 매 작업에 읽히지 않으므로 누적되어도 per-task 비용이 거의 없다.
- **폐기는 압축이 아니라 상태로 처리한다.** 결정이 무효화되면 원문 `Status`를
  `Deprecated` 또는 `Superseded`로 바꾸고 후속 ADR을 가리킨다.
- **`ADR-Refs.md`에는 현재 구속력 있는(Active) 참조만 남긴다.** 폐기된 ADR 링크는 참조에서
  제거한다(원문은 `Decisions/`에 그대로 보존).
- **`ADR-Refs.md`는 인덱스로 유지한다.** `ADR-ID + 한 줄 영향 + 링크`만 두고, 상세는 원문으로 확인한다.

## 정리 주기 (이벤트 구동 + 주기 백스톱)

- **이벤트 구동(주):** ADR을 supersede/폐기하거나 기능을 제거하는 그 시점에 `ADR-Refs.md`와
  `CONTEXT.md`를 즉시 정리한다.
- **주기 백스톱(보조):** 마일스톤/스프린트 종료 시 죽은 링크·예산 초과 문서·폐기된 잔존 참조를 점검한다.

## Allowed Exceptions

<!-- TODO: 사소한 오타 수정 등 문서 갱신을 생략할 수 있는 기준을 작성한다. -->
- 의미 변화가 없는 오타/서식 수정은 문서 갱신 기록을 생략할 수 있다.

## Validation

<!-- TODO: 문서 링크/구조 점검 방법을 작성한다. 검증 도구는 ../Validation/README.md 참고. -->
- 죽은 참조·경로는 `python Tools/validate-doc-links.py`로 점검한다(선택 도구).
- 자동 실행이 어려우면 `../Validation/manual-checklist.md`로 대체한다.

## Related Documents

- `./README.md`
- `../Validation/README.md`
- `../WorkLogs/README.md`
