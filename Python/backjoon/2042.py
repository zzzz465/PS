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

tree_height = get_tree_height(N)
tree = [None] * (2 ** tree_height)

def insert(start: int, end: int, index: int, value: int):
    if start == index:
        tree[start] = value

    mid = (start + end) // 2

    if index > (mid + 1):
        return insert(mid + 1, end, index, value)
    else:
        return insert(start, mid, index, value)

for i in range(N):
    int(input())
