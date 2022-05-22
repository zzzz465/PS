from collections import deque
import sys
from typing import List, Set, TextIO

EMap = List[Set[int]]


def parse_input(io: TextIO):
    V, E = map(int, io.readline().split())

    eMap: EMap = [set() for _ in range(20001)]

    for _ in range(E):
        u, v = map(int, io.readline().split())

        eMap[u].add(v)
        eMap[v].add(u)

    return V, E, eMap


def solve(V: int, E: int, eMap: EMap) -> str:
    vMarkers = [0] * (V + 1)

    q = deque([1])
    vMarkers[1] = 1

    while len(q) > 0:
        curr = q.popleft()

        curr_state = vMarkers[curr]
        new_state = 0

        if curr_state == 0:
            continue
        elif curr_state == 1:
            new_state = 2
        else:
            new_state = 1

        for other in eMap[curr]:
            if vMarkers[other] == 0:
                vMarkers[other] = new_state
                q.append(other)
            elif vMarkers[other] == curr_state:
                # 같은 것 끼리 간선이 있음 -> 이분 그래프가 아님
                return "NO"

    valid = all(vMarkers[1:])

    if valid:
        return "YES"
    else:
        return "NO"


def main():
    K = int(input())

    for _ in range(K):
        V, E, eMap = parse_input(sys.stdin)

        print(solve(V, E, eMap))


main()
