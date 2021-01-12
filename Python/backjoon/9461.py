memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 3,
    7: 4,
    8: 5,
    9: 7,
    10: 9
}

def solve(n):
    if n not in memo:
        memo[n] = solve(n-1) + solve(n - 5)

    return memo[n]

N = int(input())

for _ in range(N):
    num = int(input())

    print(solve(num))