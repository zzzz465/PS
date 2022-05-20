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
from typing import List, Literal, NamedTuple, Optional, Union, cast


WALL = Literal["#"]
HOLE = Literal["O"]
MARBLE_R = Literal["R"]
MARBLE_B = Literal["B"]
NONE = Literal["."]

Value = Union[WALL, HOLE, MARBLE_R, MARBLE_B, NONE]

Matrix = List[List[Value]]
Point = NamedTuple("Point", [("y", int), ("x", int)])


def mat_find(mat: Matrix, value: Value) -> Optional[Point]:
    for y, li in enumerate(mat):
        for x, val in enumerate(li):
            if val == value:
                return Point(y, x)

    return None


def mat_get(mat: Matrix, p: Point) -> Value:
    return mat[p.y][p.x]


def mat_valid(r_p: Point, b_p: Point, mat: Matrix):
    def _check_in_wall(p: Point):
        x = mat_get(mat, p)

        return x == WALL

    def _check_in_hole(p: Point):
        x = mat_get(mat, p)

        return x == HOLE

    if _check_in_wall(r_p):
        return False
    elif _check_in_wall(b_p):
        return False
    elif _check_in_hole(b_p):
        return False
    elif r_p == b_p:
        return False

    return True


def solve(N: int, M: int, mat: Matrix):

    pass


def main():
    N, M = map(int, input().split())

    # N * M matrix
    mat: List[List[Value]] = cast(List[List[Value]], [list(input().split()) for _ in range(N)])

    print(solve(N, M, mat))
