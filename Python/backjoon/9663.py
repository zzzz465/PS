N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

total = 0

directions = [
    (1, -1), (1, 1) # 윗쪽으로 가는건 없어도 무방
]

def add(y: int, x: int, flag: int) -> None:
    for i in range(N):
        board[i][x] += flag
        board[y][i] += flag

        for direction in directions:
            newY, newX = y + i * direction[0], x + i * direction[1]
            if 0 <= newY < N and 0 <= newX < N:
                board[newY][newX] += flag

def solve(y, x, count):
    global total

    if count == 0:
        total += 1
        return

    for j in range(0, N):
        if board[y][j] == 0:
            add(y, j, 1)
            solve(y + 1, j, count - 1)
            add(y, j, -1)

solve(-1, -1, N)
print(total)