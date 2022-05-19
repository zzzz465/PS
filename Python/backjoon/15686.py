from typing import List, Tuple


N, M = map(int, input().split())

mat = [*map([*map(int, input().split())], range(N))]

Point = Tuple[int, int]

CHICKEN = 2
HOUSE = 1

chickens: List[Point] = []
houses: List[Point] = []

for y, li in enumerate(mat):
    for x, val in enumerate(li):
        p: Point = (y, x)
        if val == CHICKEN:
            chickens.append(p)
        elif val == HOUSE:
            houses.append(p)


def dist(p1: Point, p2: Point) -> int:
    d1 = abs(p1[0] - p2[0])
    d2 = abs(p1[1] - p2[1])

    return d1 + d2
