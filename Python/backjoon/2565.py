from typing import List, Tuple

N = int(input())
lines: List[Tuple[int, int]] = [None] * N
for i in range(N):
    lines[i] = tuple(map(int, input().split()))

lines.sort(key=lambda x: x[0])

memo = dict()

def solve(x: int, y: int, index: int) -> int:
    if index >= N:
        return 0

    if (x, y, index) not in memo:
        newX, newY = lines[index]
    
        if (newX < x and newY > y) or (newX > x and newY < y):
            return solve(x, y, index + 1) + 1 # 꼬였을 경우 버림
    
        minimum = solve(x, y, index + 1) + 1 # 버리고 갔을 경우
        minimum = min(minimum, solve(newX, newY, index + 1)) # 선택했을 경우

        memo[(x, y, index)] = minimum

    return memo[(x, y, index)]

minimum = 987654321

for i in range(N):
    result = solve(0, 0, 0)
    minimum = min(minimum, result)

print(minimum)
    