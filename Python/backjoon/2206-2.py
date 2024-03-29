N, M = map(int, input().split())

arr = [None] * N

for i in range(N):
    arr[i] = list(map(int, [*input()]))

VALID_TILE = 0
INVALID_TILE = 1

# 좌측 상단 (1, 1) 에서 우측 하단 (N, N) 으로 도달하는 최소한의 거리

from collections import defaultdict, deque
import sys
from typing import Dict, List, Tuple

# Tuple<y: int, x: int, score: int, pickaxe_used: bool>
queue = deque()

# List<List<[int, int]> y, x, break 에 대한 3차원 배열
visited: List[List[List[int]]] = [None] * N

for y in range(N):
    visited[y] = [[sys.maxsize, sys.maxsize] for _ in range(M)]

queue.append((0, 0, 0, False))

max_score = -sys.maxsize

def visit(y: int, x: int, score: int, pickaxe_used: int):
    global max_score

    # is valid?
    if y < 0 or y >= N or x < 0 or x >= M:
        return

    if arr[y][x] == INVALID_TILE:
        if not pickaxe_used:
            queue.append((y, x, score + 1, True))
            visited[y][x][1] = score + 1
    else:
        queue.append((y, x, score + 1, pickaxe_used))
        visited[y][x][pickaxe_used] = score + 1

while len(queue) > 0:
    y, x, score, pickaxe_used = queue.popleft()

    # print(f'visit {(y, x)}, score: {score}, used: {pickaxe_used}')

    if y == N - 1 and x == M - 1:
        print(score + 1)
        exit(0)

    # up
    visit(y - 1, x, score, pickaxe_used)
    
    # right
    visit(y, x + 1, score, pickaxe_used)

    # down
    visit(y + 1, x, score, pickaxe_used)

    # left
    visit(y, x - 1, score, pickaxe_used)

print(-1)