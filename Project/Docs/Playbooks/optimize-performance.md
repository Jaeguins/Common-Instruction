# Playbook: 성능 최적화

## When To Use
프레임/메모리/로딩 등 성능을 개선해야 할 때 사용한다.

## Required Reading
- `../ProjectRules/performance-policy.md`

## Procedure
1. 목표 지표와 측정 기준을 확인한다.
2. 프로파일링으로 현재 수치와 핫스팟을 측정한다.
3. 가장 영향이 큰 병목부터 개선한다.
4. 변경 전후를 동일 조건에서 재측정한다.

## Validation
- 목표 지표 충족 여부를 측정으로 확인한다.
- 다른 영역에 성능 회귀가 없는지 확인한다.

## Output
- 최적화 변경
- 영향도가 크면 `../WorkLogs/`에 측정 수치 포함 작업 로그 기록

## Related Documents
- `../ProjectRules/performance-policy.md`
