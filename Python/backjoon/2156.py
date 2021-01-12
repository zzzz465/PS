N = int(input())

import sys
sys.setrecursionlimit(1000000)

wines = [0] * N

for i in range(N):
    wines[i] = int(input())

memo = dict()

def solve(select: int, count: int) -> int:
    if select < N:
        if (select, count) not in memo:
            result = solve(select + 1, 2) # 이번 잔을 스킵 -> 제한 초기화
            if count > 0:
                result = max(result, wines[select] + solve(select + 1, count - 1)) # 이번 잔을 마심

            memo[(select, count)] = result
            return result

        else:
            return memo[(select, count)]

    else:
        return 0

print(solve(0, 2))