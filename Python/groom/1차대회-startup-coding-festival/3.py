from typing import Tuple
from collections import defaultdict

N = int(input())
matrix = [[*map(int, [*input()])] for _ in range(N)]

def canPlace(size: int, pos: Tuple[int]): # pos -> left top of the box
    for i in range(size):
        for j in range(size):
            y = pos[1] + i
            x = pos[0] + j
    
            if not (0 <= y < N and 0 <= x < N and matrix[y][x] == 1):
                return False

    return True

size = 1
counter = defaultdict(int)
while True:
    placed = False
    for y in range(N):
        for x in range(N):
            if canPlace(size, [y, x]):
                counter[size] += 1
                placed = True

    if not placed:
        break
    else:
        size += 1

print(f'total: {sum(counter.values())}')
for pair in counter.items():
    size, count = pair
    print(f'size[{size}]: {count}')