import heapq


N, M, K = map(int, input().split())

'''
N: 수의 개수
M: 변경 횟수
K: 구간의 합을 구하는 횟수

B+ tree 를 구현하면 될 것 같지 않은가?
'''

tree = []

def leaf_depth(leaf_count: int):
    count = 0
    while leaf_count > 0:
        leaf_count = leaf_count // 2
        count += 1
    
    return count

print(leaf_depth(1))

def insert(index: int, value: int):

    pass

for i in range(N):
    int(input())
