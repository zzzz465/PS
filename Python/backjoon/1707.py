from io import StringIO
import sys
from typing import Any, Callable, Iterable, List, Set, TextIO, Tuple, TypeVar
import unittest

Vertice = Tuple[int, int]
TypeReturn = TypeVar("Return")


def solve(vertices: List[Vertice]) -> bool:
    Group = Set[int]

    g1: Group = set()
    g2: Group = set()

    for u, v in vertices:
        if u not in g1 and u not in g2:
            g1.add(u)
            g2.add(v)
        else:
            if u in g1:
                g2.add(v)
            else:
                g1.add(v)

    return len(g1.intersection(g2)) == 0


def parse_input(io: TextIO):
    K = int(io.readline())

    verticesArr: List[List[Vertice]] = []

    for _ in range(K):
        V, E = map(int, io.readline().split())
        vertices: List[Tuple[int, int]] = list()

        for _ in range(E):
            u, v = map(int, io.readline().split())
            vertices.append((u, v))

        verticesArr.append(vertices)

    return verticesArr


def main():
    verticesArr = parse_input(sys.stdin)

    for vertices in verticesArr:
        res = solve(vertices)

        if res:
            print("YES")
        else:
            print("NO")


test_cases = [
    (
        """
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
    """,
        (True, False),
    ),
    (
        """
        1
5 4
1 2
3 4
3 5
4 5
        """,
        (True),
    ),
]


class TestCase(unittest.TestCase):
    def __init__(self, vertices: List[Vertice], expected: bool) -> None:
        self.vertices = vertices
        self.expected = expected

        super().__init__(self.test_run.__name__)

    def test_run(self):
        res = solve(self.vertices)
        self.assertEqual(res, self.expected)


# what is "..."? https://seungwubaek.github.io/tools/numpy/ellipsis/
def apply(func: Callable[..., TypeReturn]) -> Callable[..., TypeReturn]:
    def _apply(args: Iterable[Any]) -> TypeReturn:
        return func(*args)

    return _apply


def parse_tc(raw: str, expected: List[bool]) -> List[TestCase]:
    verticesArr = parse_input(StringIO(raw.strip()))

    test_cases: List[TestCase] = []

    for i, vertices in enumerate(verticesArr):
        test_cases.append(TestCase(vertices, expected[i]))

    return test_cases


def runTest():
    tcs = list(map(apply(parse_tc), test_cases))
    suite = unittest.TestSuite([tc for sub in tcs for tc in sub])

    unittest.TextTestRunner().run(suite)


main()
# runTest()
