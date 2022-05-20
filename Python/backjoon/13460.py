"""
보드 크기는 N x M (세로 x 가로)

- 보드에는 구멍이 단 한개 있음
- 빨간 구슬, 파란 구슬 하나가 있음
- 벽은 막혀있음
- 파란 구슬을 구멍에 빠트리면 안됨
- 빨간 구술을 보드에서 빼내야 함 -> 구멍으로 빨간 구슬을 넣어야 함
- 상하좌우로 굴리기 가능 (모든 구슬은 동시에 굴러감)
- 최소 횟수로 빨간 구술 꺼내기

상태와 관련된 BFS 를 수행하면 될 듯
"""

from enum import Enum
from typing import List


class Value(Enum):
    WALL = "#"
    HOLE = "O"
    MARBLE_R = "R"
    MARBLE_B = "B"
    NONE = "."


Matrix = List[List[Value]]


def mat_valid(mat: Matrix):

    pass


def solve(N: int, M: int, mat: Matrix):

    pass


def main():
    N, M = map(int, input().split())

    # N * M matrix
    mat: List[List[Value]] = [list(map(lambda x: Value(x), input().split())) for _ in range(N)]

    print(solve(N, M, mat))
