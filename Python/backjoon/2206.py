from typing import Deque, List, Tuple
from collections import deque, namedtuple

N, M = map(int, input().split())

board = [[None for _ in range(M)] for _ in range(N)]

for i in range(N):
    text = input()
    for j in range(M):
        board[i][j] = int(text[j])

# 안 깼을 경우 체크하고, 깼을 경우, 어디를 깨야 할까?
# BFS? 굳이 윗쪽으로?

# 부술 수 있는 벽들
Pos = namedtuple('Pos', ['x', 'y', 'breakCount'])

queue = deque()
queue.append(Pos(0, 0, 0))

visit = [[[-1, -1] for _ in range(M)] for _ in range(N)]
visit[0][0] = [0, -1]

def isValid(x: int, y: int):
    return 0 <= x and x < M and 0 <= y and y < N

reach = False

while len(queue) > 0:
    x, y, breakCount = queue.popleft()

    for offsetX, offsetY in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newX, newY = x + offsetX, y + offsetY

        if isValid(newX, newY):
            if board[newY][newX] == 0 and visit[newY][newX][breakCount] == -1:
                visit[newY][newX][breakCount] = visit[y][x][breakCount] + 1
                queue.append(Pos(newX, newY, breakCount))

            if board[newY][newX] == 1 and breakCount == 0:
                breakCount += 1
                visit[newY][newX][breakCount] = visit[y][x][breakCount - 1] + 1
                queue.append(Pos(newX, newY, breakCount))

result = visit[N-1][M-1]
if result[0] == -1 and result[1] != -1:
    print(result[1])
elif result[0] != -1 and result[1] == -1:
    print(result[0])
else:
    print(min(result))
                
                