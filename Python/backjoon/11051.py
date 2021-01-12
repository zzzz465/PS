import sys

sys.setrecursionlimit(100000)

n, k = [*map(int, input().split())]

memo = dict()

def factorial(n):
    if n == 1 or n == 0:
        return 1

    if n not in memo:
        memo[n] = n * factorial(n - 1)
    
    return memo[n]

def solve(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    
    if (n, k) not in memo:
        memo[(n, k)] = solve(n-1, k) + solve(n-1, k-1)

    return memo[(n, k)]


print(solve(n, k) % 10007)