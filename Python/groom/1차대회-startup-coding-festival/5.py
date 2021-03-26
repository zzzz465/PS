from typing import Tuple
from collections import deque
from sys import maxsize

# c 는 최상단에만 있고, 최하단으로 이동해야함, 좌-우 이동이 가장 짧은 것을 선택

N, M = map(int, input().split())

# test values
# N = 20
# M = 1000
# matrix = ['c' * N] + ['.' * N for _ in range(M-1)]
# matrix = ['c' * N] + ['.' * N for _ in range(M-2)] + ['x' * N]

matrix = [input() for _ in range(M)]
cache = [[-1] * N for _ in range(M)]

def BFS(start: Tuple[int]):
    for i in range(M):
        for j in range(N):
            cache[i][j] = -1

    minimum = 1250
    q = deque()
    q.append((0, (start[0], start[1]))) # add initial position

    while len(q) > 0:
        score, pos = q.popleft()
        y, x = pos

        # print(f'score: {score} pos: {pos}')

        if matrix[y][x] == 'x':
            continue
        
        elif score >= minimum:
            continue

        elif cache[y][x] != -1: # 이미 지나갔고, 더 스코어가 클 경우
            continue
        
        elif y == M - 1: # 도달
            minimum = min(minimum, score)
            break

        else:
            cache[y][x] = score

            if x > 0: # left
                q.append((score + 1, (y, x - 1)))

            if x < N - 1: # right
                q.append((score + 1, (y, x + 1)))

            if y < M - 1: # down
                q.append((score, (y + 1, x)))

    return minimum if minimum != 1250 else -1

minimumValue = maxsize
for i in range(N):
    if matrix[0][i] == 'c':
        print(f'doing 0, {i}')
        minimumValue = min(minimumValue, BFS((0, i)))

print(minimumValue)