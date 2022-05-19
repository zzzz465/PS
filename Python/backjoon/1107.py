import sys
from typing import Generator, Iterable, List, Tuple


N = int(input())
M = int(input())
broken_buttons: List[int] = list()

if 0 < M:
    broken_buttons = list(map(int, input().split()))

available_buttons = sorted({1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - set(broken_buttons))

# 1. 사용 가능한 수로 N이랑 최대한 가까운 수 만들기

Delta = int
DeltaTuple = Tuple[Delta, int]


def values_by_delta(
    target: int, values: Iterable[int]
) -> Generator[DeltaTuple, None, None]:
    # values 를 target 에 대한 delta 순으로 오름차순 정렬한 배열을 반환
    deltas = list(map(lambda x: (abs(target - x), x), values))

    deltas.sort()

    for delta in deltas:
        yield delta


def build_values(target: str, values: List[int]) -> Generator[str, None, None]:
    x = int(target[0])

    for delta in values_by_delta(x, values):
        if len(target[1:]) == 0:
            yield str(delta[1])
        else:
            for sub in build_values(target[1:], values):
                yield str(delta[1]) + sub


min_diff = sys.maxsize
min_val = sys.maxsize

for value in map(int, build_values(str(N), available_buttons)):
    diff = abs(N - value)

    if diff < min_diff:
        min_diff = diff
        min_val = value

button_input_count = len(str(min_val))

if min_diff + button_input_count > abs(N - 100):
    # 시작 지점에서 +, - 으로 이동하는 것이 더 빠름
    print(abs(N - 100))
else:
    # 새로운 시작 지점에서 이동하는 것이 빠름
    print(abs(N - min_val) + button_input_count)
