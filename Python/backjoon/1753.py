from collections import defaultdict, deque
import heapq
import sys
from typing import Dict, List, Set, Tuple


V, E = map(int, input().split())

# start
K = int(input())

# Dict<u, Tuple<v, w>>
edges: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

for i in range(E):
    u, v, u = map(int, input().split())

    edges[u].append((v, u))

vertices: List[int] = [sys.maxsize for _ in range(V + 1)]
vertices[K] = 0
visited: Set[int] = set()

hq = []
heapq.heappush(hq, (0, K))

while len(hq) > 0:
    _, u = hq.popleft()

    if u in visited:
        continue
    else:
        visited.add(u)

    vwArr = edges[u]

    for (v, w) in vwArr:
        vertices[v] = max(vertices[v], vertices[u] + w)
        heapq.heappush(hq, (vertices[v], v))

for i in range(1, V + 1):
    if vertices[i] == sys.maxsize:
        print('INF')
    else:
        print(vertices[i])
