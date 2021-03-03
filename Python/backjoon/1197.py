import heapq
from typing import Set

## 메모리 초과!!

V, E = map(int, input().split())

edges = []
vertices = [[False for _ in range(V + 1)] for _ in range(V + 1)]

# add edges into heap
for i in range(E):
    a, b, w = map(int, input().split())
    heapq.heappush(edges, (w, a, b))

def isConnected(a: int, b: int) -> bool:
    def _findWithDFS(root: int, target: int, memo: Set[int]):
        global vertices

        if root == target:
            return True

        if root in memo:
            return False
        else:
            memo.add(root)

        for i in range(1, V + 1):
            if vertices[root][i]: # connected
                connected = _findWithDFS(i, target, memo)
                if connected:
                    return True

        return False

    return _findWithDFS(a, b, set())

def connect(a: int, b: int) -> None:
    vertices[a][b] = True
    vertices[b][a] = True

# edge 정렬
weightSum = 0
for edge in edges:
    a, b, weight = edge
    if not isConnected(a, b):
        connect(a, b)
        weightSum += weight

print(weightSum)