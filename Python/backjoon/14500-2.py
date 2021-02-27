N, M = map(int, input().split())

board = [None] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

patterns = (
    ( (0, 0), ())
)