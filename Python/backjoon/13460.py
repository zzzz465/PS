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
from collections import defaultdict, deque
from io import StringIO
import operator
import sys
from typing import IO, Deque, Dict, List, Literal, NamedTuple, Optional, Tuple, Union, cast
import unittest


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


def mat_set(mat: Matrix, p: Point, value: Value) -> None:
    mat[p.y][p.x] = value


def mat_valid(r_p: Point, b_p: Point, mat: Matrix) -> bool:
    def _check_bound(p: Point):  # return true if p is out of bound
        h = len(mat)
        w = len(mat[0])

        if not (0 <= p.y < h):
            return True
        elif not (0 <= p.x < w):
            return True

        return False

    def _check_in_wall(p: Point):
        x = mat_get(mat, p)

        return x == WALL

    def _check_in_hole(p: Point):
        x = mat_get(mat, p)

        return x == HOLE

    if _check_bound(r_p):
        return False
    elif _check_in_wall(r_p):
        return False

    if _check_bound(b_p):
        return False
    elif _check_in_wall(b_p):
        return False
    elif _check_in_hole(b_p):
        return False

    if r_p == b_p:
        # 구슬이 같이 있음 = 구멍에 둘다 빠진 상황
        return False

    return True


# (y, x), Up, Right, Down, Left
dir_map = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move(p: Point, dir: int, mat: Matrix, other: Point) -> Point:
    """
    실패 요인:
    1. 구슬을 한 칸씩 이동시키는 것이 아니고, 계속 기울여서 벽에 닿을 때 까지 굴리는 것이다.
        이것을 제대로 구현하지 않았음 (문제를 잘 읽자...)
    2. 구슬이 동시에 빠지는 것을 고려하지 않음
    """

    new_y, new_x = p.y, p.x
    new_p = p

    while True:
        v = mat_get(mat, Point(new_y, new_x))

        if new_p == other:
            if v == "O":
                p = new_p
            break
        else:
            if v == "#":
                break
            elif v == "O":
                p = new_p
                break
            elif v == ".":
                p = new_p

        new_y, new_x = map(operator.add, p, dir_map[dir])
        new_p = Point(new_y, new_x)

    return p


def solve(N: int, M: int, mat: Matrix) -> int:
    # define initial values
    Record = NamedTuple("Record", (("r", Point), ("b", Point)))
    Cost = int
    state: Dict[Record, int] = defaultdict(lambda: sys.maxsize)
    min_cost = sys.maxsize

    hole = mat_find(mat, "O")
    if not hole:
        raise Exception()

    init_b_p = mat_find(mat, "B")
    if not init_b_p:
        raise Exception()
    mat_set(mat, init_b_p, ".")

    init_r_p = mat_find(mat, "R")
    if not init_r_p:
        raise Exception()
    mat_set(mat, init_r_p, ".")

    # finding optimal cost using BFS
    q: Deque[Tuple[Record, Cost]] = deque([(Record(init_r_p, init_b_p), 0)])

    while len(q) > 0:
        curr, cost = q.popleft()

        if cost > 10:
            # 실패 요인: 문제 조건에 10번 이하로 불가능하면 -1 을 출력하라고 명시되어 있었음
            continue

        if curr.r == hole:
            min_cost = min(cost, min_cost)
            continue

        cost += 1

        for i in range(0, 4):
            # 충돌 때문에 한 쪽을 두번 갱신해야 함
            # n >= 2, n 번 호출해도 결과는 같음
            new_r_p = move(curr.r, i, mat, curr.b)
            new_b_p = move(curr.b, i, mat, new_r_p)
            new_r_p = move(new_r_p, i, mat, new_b_p)

            if not mat_valid(new_r_p, new_b_p, mat):
                continue

            key = Record(new_r_p, new_b_p)
            memo_cost = state[key]
            if cost < memo_cost:
                state[key] = cost
                q.append((key, cost))

    if min_cost == sys.maxsize:
        return -1
    else:
        return min_cost


def parse_input(io: IO[str]) -> Tuple[int, int, Matrix]:
    N, M = map(int, io.readline().split())

    # N * M matrix
    mat: Matrix = cast(Matrix, [list(io.readline()) for _ in range(N)])

    return N, M, mat


def main() -> None:
    N, M, mat = parse_input(sys.stdin)

    print(solve(N, M, mat))


class TestCase(unittest.TestCase):
    N: int
    M: int
    mat: Matrix
    expected: int

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(self.test_solve.__name__)

    def test_solve(self):
        res = solve(self.N, self.M, self.mat)
        self.assertEqual(res, self.expected)


def parse_tc(tc_raw: str, expected: int) -> TestCase:
    # https://dongyeopblog.wordpress.com/2016/06/13/python-stringio-%ED%8C%8C%EC%9D%BC%EB%A1%9C-%EC%9D%BD%EA%B8%B0%EC%93%B0%EA%B8%B0/
    io = StringIO(tc_raw.strip())  # rstrip 포함하면 termination 안이뤄져서 stdin 대기함 -> 아님
    io.seek(0)
    N, M, mat = parse_input(io)
    tc = TestCase()

    tc.N = N
    tc.M = M
    tc.mat = mat
    tc.expected = expected

    return tc


def run_test() -> None:
    tcs = [
        (
            """
5 5
#####
#..B#
#.#.#
#RO.#
#####
""",
            1,
        ),
        (
            """
            7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
            """,
            5,
        ),
        (
            """
            7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######
            """,
            5,
        ),
        (
            """
            10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########
            """,
            -1,
        ),
        (
            """
            3 7
#######
#R.O.B#
#######
            """,
            1,
        ),
        (
            """
            10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########
            """,
            7,
        ),
        (
            """
3 10
##########
#.O....RB#
##########
            """,
            -1,
        ),
        (
            """
7 5
#####
###.#
##.O#
#R..#
#####
###B#
#####
            """,
            2,
        ),
        (
            """
5 10
##########
#.#......#
##.......#
#OR..B.#.#
##########
            """,
            7,
        ),
        (
            """
4 7
#######
##R...#
#O.#.B#
#######
            """,
            2,
        ),
        (
            """
7 4
####
#B##
####
#.##
#R##
#O##
####
            """,
            1,
        ),
        (
            """
10 5
#####
#..##
#.O##
#...#
#.R##
##.##
##.##
#.###
#.B.#
#####
            """,
            1,
        ),
        (
            """
            3 6
######
#.ORB#
######
            """,
            -1,
        ),
        (
            """
            8 8
########
#.####.#
#...#B##
#.##.R.#
######.#
##.##O.#
###.##.#
########
            """,
            7,
        ),
        (
            """
            4 6
######
#R####
#B..O#
######
            """,
            -1,
        ),
        (
            """
            4 6
######
#R#O##
#B...#
######
            """,
            4,
        ),
    ]

    suite = unittest.TestSuite([parse_tc(*x) for x in tcs])

    unittest.TextTestRunner().run(suite)


main()
# run_test()
