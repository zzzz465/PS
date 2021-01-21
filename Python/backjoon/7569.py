M, N, H = map(int, input().split())

# z y x 순으로 접근
box = [[[None for _ in range(M)] for _ in range(N)] for _ in range(H)]
enclosed = []
youngExist = False

for i in range(H):
    for j in range(N):
        numbers = [*map(int, input().split())]
        for k in range(M):
            box[i][j][k] = numbers[k]
            if (numbers[k] == 0):
                youngExist = True

if not youngExist:
    print(0)
    exit(0)

from collections import deque

queue = deque()

directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                for offsetX, offsetY, offsetZ in directions:
                    newZ, newY, newX = i + offsetZ, j + offsetY, k + offsetX

                    if 0 <= newZ < H and 0 <= newY < N and 0 <= newX < M:
                        if box[newZ][newY][newX] == 0:
                            queue.append((newZ, newY, newX))

while queue:
    z, y, x = queue.pop()

    for offsetX, offsetY, offsetZ in directions:
        newZ, newY, newX = z + offsetZ, y + offsetY, x + offsetX

        if 0 <= newZ < H and 0 <= newY < N and 0 <= newX < M:
            if box[newZ][newY][newX] == 0 or box[newZ][newY][newX] > box[z][y][x]:
                box[newZ][newY][newX] = box[z][y][x] + 1
                queue.append((newZ, newY, newX))

done = True
import sys
maxVal = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                done = False
                break
            else:
                maxVal = max(maxVal, box[i][j][k])

if done: # 전부 다 익었음
    print(maxVal)
else:
    print(-1)