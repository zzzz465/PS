import heapq


N, M, K = map(int, input().split())

'''
N: 수의 개수
M: 변경 횟수
K: 구간의 합을 구하는 횟수

B+ tree 를 구현하면 될 것 같지 않은가?
'''

tree = []

def leaf_depth():
    _N = N
    count = 0
    while _N > 0:
        _N = _N // 2
        count += 1
    pass

def insert(index: int, value: int):

    pass

for i in range(N):
    int(input())
