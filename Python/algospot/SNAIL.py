import sys

C = int(input())

# 비가 올 확률 75%


for _ in range(C):
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))

    memo = 

    def solve(left, days):
        if left <= 0:
            return 1

        if days <= 0:
            return left <= 0

        if (left, days) not in memo:
            result = 0
            result += 0.75 * solve(left - 2, days - 1)
            result += 0.25 * solve(left - 1, days - 1)

            memo[(left, days)] = result

        return memo[(left, days)]

    print(solve(n, m))