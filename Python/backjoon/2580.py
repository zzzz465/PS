
from typing import List, Tuple


board = [None] * 9
zeros = []
for i in range(9):
    board[i] = list(map(int, input().split()))

    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))

def availableNumbers(pos: Tuple[int, int]):
    y, x = pos
    numbers = [True for i in range(10)] # 0 ~ 10, 0은 쓸모X
    for i in range(9):
        numbers[board[y][i]] = False
        numbers[board[i][x]] = False

    y = y // 3
    x = x // 3
    for i in range(3):
        for j in range(3):
            val = board[y * 3 + i][x * 3 + j]
            numbers[val] = False

    result = []
    for i in range(1, 10):
        if numbers[i]:
            result.append(i)

    return result

def solve(remaining: List[Tuple[int, int]]):
    if len(remaining) == 0:
        for line in board:
            print(' '.join(map(str, line)))
        exit(0)

    top = remaining.pop()
    y, x = top
    numbers = availableNumbers(top)
    
    for num in numbers:
        board[y][x] = num
        solve(remaining)
        board[y][x] = 0

    remaining.append(top)

solve(zeros)