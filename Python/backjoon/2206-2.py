N, M = map(int, input().split())

arr = [None] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

VALID_TILE = 0
INVALID_TILE = 1

# 좌측 상단 (1, 1) 에서 우측 하단 (N, N) 으로 도달하는 최소한의 거리

from collections import deque
from typing import Set, Tuple

# Tuple<y: int, x: int, score: int, pickaxe_used: bool>
queue = deque()
visited: Set[Tuple[int, int]] = set()

queue.append(())

def visit(y: int, x: int, score: )

while len(queue) > 0:
    score, breaked, y, x = queue.popleft()

    if (y, x) in visited:
        continue
