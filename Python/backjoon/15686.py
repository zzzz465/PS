from re import T
import sys
from typing import List, Tuple
from itertools import combinations

N, M = map(int, input().split())

mat = [[*map(int, input().split())] for _ in range(N)]

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


'''
house 순회하며 chicken 선택해서 전체 탐색?
그런데, 치킨 집은 최대 M개만 선택 가능

house -> chicken 에 cost 저장하고 필터링?
(도달한 치킨 집 개수)
'''

Mat = List[List[T]]

visit_mat: Mat[Point] = [[map() for _ in range(N)] for _ in range(N)]

for house_p in houses:
    for chicken_p in chickens:
        d = dist(house_p, chicken_p)
        y, x = chicken_p

        visit_mat[y][x]

min_score = sys.maxsize

for i in range(1, M):
    combs = list(combinations(chickens, i))

    for comb in combs:
        score_sum = sum(map(lambda x: visit_mat[x[0]][x[1]], comb))
        min_score = min(score_sum, min_score)


print(min_score)
