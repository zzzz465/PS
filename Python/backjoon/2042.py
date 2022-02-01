from typing import Optional


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
tree = [(0, False)] * (2 ** (tree_height + 1) + 1)  # starts from 1

'''
leaf_start:  leaf node range start
leaf_end:    leaf node range end, leaf_start ~ leaf_end must be 2^n
node:   current node index
index:  target leaf node index
value:  value to assign to leaf_node[index]

N 개의 leaf node 에서, index K 를 업데이트 하는 방법
update(0, N-1, 1, K, value) # 0, N-1, 1, K 는 고정
'''


def update(index: int, value: int):
    return updateInternal(leaf_start=1, leaf_end=2 ** (tree_height - 1), node=1, index=index, value=value)


def updateInternal(leaf_start: int, leaf_end: int, node: int, index: int, value: int):
    print(f'update start: {leaf_start} end: {leaf_end} node: {node} index: {index} value: {value}')

    if leaf_start == leaf_end:
        tree[node] = value
        return

    invalidate(node)

    mid = (leaf_start + leaf_end) // 2

    if index <= mid: # left
        return updateInternal(leaf_start, mid, node * 2, index, value)
    else: # right
        return updateInternal(mid + 1, leaf_end, node * 2 + 1, index, value)


def invalidate(node: int):
    tree[node] = (tree[node][0], False)


def setNode(node: int, value: int):
    tree[node] = (value, True)


'''
get value of index, memo partial sum.
'''


def get(start: int, end: int) -> bool:
    return getInternal(tree_start=1, tree_end=2 ** (tree_height - 1), range_start=start, range_end=end, node=1)


def getInternal(tree_start: int, tree_end: int, range_start: int, range_end: int, node: int) -> int:
    if range_start > range_end or tree_start > range_end:
        return 0
    elif tree_start > range_end or tree_end < range_start:
        return 0

    if tree_start == tree_end: # leaf node
        return tree[tree_start]

    if dirty(node):
        value: Optional[int] = None

        # 1. tree start ~ end 사이에 range 가 들어가 있을 경우
        if tree_start <= range_start and range_end <= tree_end:
            tree_mid = (tree_start + tree_end) // 2
            left = getInternal(tree_start, tree_mid, range_start, range_end, node * 2)
            right = getInternal(tree_mid + 1, tree_end, range_start, range_end, node * 2 + 1)

            value = left + right

        # 2. tree start ~ end 밖에 range 가 들어가 있을 경우
        elif tree_start > range_end or tree_end < range_start:
            value = 0

        # 3. tree start ~ end 와 range start ~ end 가 걸쳐 있을 경우
        # 윗 쪽에서, 서로 range start ~ end 의 역전이 일어났는 지를 검사한다
        else:
            tree_mid = (tree_start + tree_end) // 2

            left = getInternal(tree_start, tree_mid, range_start, tree_mid, node * 2)
            right = getInternal(tree_mid + 1, tree_end, tree_mid + 1, range_end, node * 2 + 1)

            value = left + right

        setNode(node, value)

    return tree[node][0]


def dirty(node: int):
    if tree[node] == None:
        return True

    return tree[node][1] == False


for i in range(1, N + 1):
    val = int(input())
    update(i, val)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b, c)
    else:
        res = get(b, c)
        print(res)
