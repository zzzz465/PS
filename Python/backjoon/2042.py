import heapq
from re import T


N, M, K = map(int, input().split())

'''
N: 수의 개수
M: 변경 횟수
K: 구간의 합을 구하는 횟수

B+ tree 를 구현하면 될 것 같지 않은가?
'''

def get_tree_height(leaf_count: int):
    if leaf_count <= 0:
        return 0

    if leaf_count == 1:
        return 1

    count = 1
    while True:
        if 2 ** count < leaf_count:
            count += 1
        else:
            return count + 1

tree = []
tree_height = get_tree_height(N)

def insert(index: int, value: int):

    pass

for i in range(N):
    int(input())
