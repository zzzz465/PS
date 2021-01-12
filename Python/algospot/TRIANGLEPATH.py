C = int(input())

for _ in range(C):
    triLen = int(input())
    tri = [list(map(int, input().split())) for _ in range(triLen)]

    memo = dict()
    def solve1(x, y):
        if y == triLen - 1:
            return tri[y][x]
        
        if (x, y) not in memo:
            memo[(x, y)] = max(solve1(x, y + 1), solve1(x + 1, y + 1)) + tri[y][x]

        return memo[(x, y)]

    print(solve1(0, 0))