memo = dict()

def solve(n):
    if n <= 2:
        return n

    if n not in memo:
        memo[n] = solve(n - 1) + solve(n - 2)

    return memo[n]

C = int(input())

for _ in range(C):
    print(solve(int(input())) % 1000000007)