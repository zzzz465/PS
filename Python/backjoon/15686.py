from typing import List, Tuple


N, M = map(int, input().split())

mat = [*map([*map(int, input().split())], range(N))]

chickens: List[Tuple[int, int]] = []
houses: List[Tuple[int, int]] = []

for y, li in enumerate(mat):
    for x, val in enumerate(li):
        pass
