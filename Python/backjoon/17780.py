# https://www.acmicpc.net/problem/17780

N, K = map(int, input().split())

board = [None] * N
for i in range(N):
    board[i] = [*map(int, input().split())]

horses = [None] * K # [[y, x, direction(1,2,3,4)]]
for i in range(K):
    horses[i] = [*map(int, input().split())]

