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
tree = [None] * (2 ** (tree_height + 1) + 1) # starts from 1

'''
start:  leaf node range start
end:    leaf node range end
node:   current node index
index:  target leaf node index
value:  value to assign to leaf_node[index]

N 개의 leaf node 에서, index K 를 업데이트 하는 방법
update(0, N-1, 1, K, value) # 0, N-1, 1, K 는 고정
'''

def update(index: int, value: int):
    return updateInternal(start=0, end=N-1, node=1, index=index, value=value)

def updateInternal(start: int, end: int, node: int, index: int, value: int):
    if start == end:
        tree[node] = value

    mid = (start + end) // 2

    if index > mid:
        return updateInternal(mid + 1, end, node * 2, index, value)
    else:
        return updateInternal(start, mid, node * 2 + 1, index, value)

'''
get value of index, memo partial sum.
'''
def getMemoizedInternal(start: int, end: int, node: int, index: int):
    if start == end:
        return tree[node]

    if not memoized(node) or dirty(node):
        pass
    pass

def memoized(node: int):
    if tree[node] == None:
        return False

    pass

def dirty(node: int):
    if tree[node] == None:
        return True
    pass

for i in range(N):
    int(input())
