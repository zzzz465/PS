from collections import defaultdict, deque
import sys
from typing import Dict, List, Set, Tuple


V, E = map(int, input().split())

# start
K = int(input())

# Dict<u, Tuple<v, w>>
edges: Dict[Tuple[int], List[Tuple[int, int]]] = defaultdict(list)

for i in range(E):
    u, v, u = map(int, input().split())

    edges.get(u).append((v, u))

vertices: List[int] = [sys.maxsize for _ in range(V + 1)]
vertices[K] = 0
visited: Set[int] = set()

q = deque()
q.append(K)

while len(q) > 0:
    u = q.popleft()

    if u in visited:
        continue

    vwArr = edges[u]

    for (v, w) in vwArr:
        vertices[v] = max(vertices[v], vertices[u] + w)

for i in range(1, V + 1):
    if vertices[i] == sys.maxsize:
        print('INF')
    else:
        print()
