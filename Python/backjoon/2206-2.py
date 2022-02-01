N, M = map(int, input().split())

arr = [None] * N

for i in range(N):
    arr[i] = list(map(int, [*input()]))

VALID_TILE = 0
INVALID_TILE = 1

# 좌측 상단 (1, 1) 에서 우측 하단 (N, N) 으로 도달하는 최소한의 거리

from collections import deque
import sys
from typing import Set, Tuple

# Tuple<y: int, x: int, score: int, pickaxe_used: bool>
queue = deque()
visited: Set[Tuple[int, int]] = set()

queue.append((0, 0, 0, False))

def visit(y: int, x: int, score: int, pickaxe_used: bool):
    # is valid?
    if y < 0 or y >= N or x < 0 or x >= M:
        return
    elif max_score != -sys.maxsize and score >= max_score:
        return

    if arr[y][x] == INVALID_TILE and not pickaxe_used:
        queue.append((y, x, score + 1, True))
    else:
        queue.append((y, x, score + 1, pickaxe_used))

max_score = -sys.maxsize

while len(queue) > 0:
    y, x, score, pickaxe_used = queue.popleft()

    if y == N - 1 and x == M - 1:
        max_score = max(max_score, score)
        continue

    # up
    visit(y - 1, x, score, pickaxe_used)
    
    # right
    visit(y, x + 1, score, pickaxe_used)

    # down
    visit(y + 1, x, score, pickaxe_used)

    # left
    visit(y, x - 1, score, pickaxe_used)

if max_score == -sys.maxsize:
    print(-1)
else:
    print(max_score)
