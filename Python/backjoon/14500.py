N, M = map(int, input().split())

board = [None] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

def find(y, x, curr, result):
    if (y, x) in curr:
        return

    curr.append((y, x))
    if len(curr) == 4:
        # 계산
        result.append(sum(map(lambda t: board[t[0]][t[1]], curr)))

    else:
        if y + 1 < N:
            find(y + 1, x, curr, result)

        if x + 1 < M:
            find(y, x + 1, curr, result)

        if x - 1 >= 0:
            find(y, x - 1, curr, result)

    curr.pop()

maxval = -1
for i in range(N):
    for j in range(M):
        res = []
        find(i, j, [], res)
        if len(res) > 0:
            maxval = max(maxval, max(res))

print(maxval)