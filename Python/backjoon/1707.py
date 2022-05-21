import sys
from typing import List, Set, TextIO, Tuple


def solve(K: int, vertices: List[Tuple[int, int]]) -> bool:
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

    return len(g1 - g2) > 0


def parse_input(io: TextIO):
    K = int(io.readline())
    vertices: List[Tuple[int, int]] = list()

    for _ in range(K):
        u, v = map(int, io.readline())
        vertices.append((u, v))

    return K, vertices


def main():
    K, vertices = parse_input(sys.stdin)

    res = solve(K, vertices)

    if res:
        print("YES")
    else:
        print("NO")


main()
