# 이 문제, 그리디구나!!!!!!!!!!
from sys import maxsize

N, M = map(int, input().split())

matrix = [input() for _ in range(M)]

min_length = maxsize

def solve(y: int, x: int):
    if y == M - 1:
        pass

    if 