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


def values_by_delta(target: int, values: Iterable[int]) -> Generator[DeltaTuple, None, None]:
    # values 를 target 에 대한 delta 순으로 오름차순 정렬한 배열을 반환
    deltas = list(map(lambda x: (abs(target - x), x), values))

    deltas.sort()

    for delta in deltas:
        yield delta


def build_values(values: List[int]) -> Generator[str, None, None]:
    def _combination(size: int, values: Iterable[int]) -> Generator[List[int], None, None]:
        if size <= 0:
            return
        else:
            for i in values:
                for j in _combination(size - 1, values):
                    yield [i] + j

    delta = 1
    while True:
        i, j = len(str(N)) - delta, len(str(N)) + delta

        for comb in _combination(i, values):
            yield "".join(map(str, comb))

        for comb in _combination(j, values):
            yield "".join(map(str, comb))

        delta += 1


min_diff = sys.maxsize
min_val = sys.maxsize

for valueStr in build_values(available_buttons):
    if len(valueStr) >= (len(str(N)) + 2):
        break

    value = int(valueStr)
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
