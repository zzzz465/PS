N, M = map(int, input().split()) # 가로 N, 세로 M

clothes = [[*map(int, input().split())] for _ in range(M)]

cache = dict()

def solve(y, x):
    if not (0 <= y < M and 0 <= x < N):
        return 0

    if (y, x) not in cache:
        res = max(solve(y-1, x), solve(y, x-1))
        cache[(y, x)] = res + clothes[y][x]

    return cache[(y, x)]

# print(solve(M-1, N-1))

clothes = [[1] * 100] * 10000

N = 100
M = 10000

print(solve(M-1, N-1))