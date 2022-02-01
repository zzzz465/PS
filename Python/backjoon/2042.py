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


# tree definition
# tree is always full(complete?) tree
tree_height: int = get_tree_height(N)
tree_leaf_node_count: int = 2 ** (tree_height - 1)
tree_nodes_count: int = 2 ** (tree_height + 1)
tree = [[0, False] for _ in range(tree_nodes_count)]  # starts from 1


def update(index: int, value: int):
    return updateInternal(tree_start=1, tree_end=tree_leaf_node_count, curr_node=1, target_index=index, value=value)


def updateInternal(tree_start: int, tree_end: int, curr_node: int, target_index: int, value: int):
    if tree_start == tree_end:
        tree[curr_node] = value
        return

    invalidate(curr_node)

    mid = (tree_start + tree_end) // 2

    if target_index <= mid:  # left
        return updateInternal(tree_start, mid, curr_node * 2, target_index, value)
    else:  # right
        return updateInternal(mid + 1, tree_end, curr_node * 2 + 1, target_index, value)


def invalidate(node: int):
    tree[node][1] = False


'''
get value of index, memo partial sum.
'''


def get(start: int, end: int) -> bool:
    return getInternal(tree_start=1, tree_end=tree_leaf_node_count, range_start=start, range_end=end, curr_node=1)


def getInternal(tree_start: int, tree_end: int, range_start: int, range_end: int, curr_node: int) -> int:
    # tree start ~ end: set A
    # range start ~ end: set B

    if range_start > range_end or tree_start > range_end:
        return 0
    elif tree_start > range_end or tree_end < range_start:
        return 0

    if tree_start == tree_end:  # leaf node
        return tree[curr_node]
    elif tree_start == range_start and tree_end == range_end and not dirty(curr_node):
        return get_node_value(curr_node)

    value: Optional[int] = None

    # 1. tree start ~ end 이 range start ~ end 을 포함할 경우 (A includes B)
    if tree_start <= range_start and range_end <= tree_end:
        tree_mid = (tree_start + tree_end) // 2
        left = getInternal(tree_start, tree_mid,
                           range_start, tree_mid, curr_node * 2)
        right = getInternal(tree_mid + 1, tree_end,
                            tree_mid + 1, range_end, curr_node * 2 + 1)

        value = left + right

    # 2. tree start ~ end 가 range start ~ end 와 전혀 연관이 없을 경우 (A intersection B = None)
    elif tree_start > range_end or tree_end < range_start:
        value = 0

    # 3. tree start ~ end 와 range start ~ end 가 걸쳐 있을 경우
    # 윗 쪽에서, 서로 range start ~ end 의 역전이 일어났는 지를 검사한다
    else:
        tree_mid = (tree_start + tree_end) // 2

        left = getInternal(tree_start, tree_mid,
                           range_start, tree_mid, curr_node * 2)
        right = getInternal(tree_mid + 1, tree_end,
                            tree_mid + 1, range_end, curr_node * 2 + 1)

        value = left + right

    # 4. B includes A
    # 존재 불가능함

    if tree_start == range_start and tree_end == range_end:
        set_node_value(curr_node, value)

    return value


def get_node_value(node: int):
    return tree[node][0]


def set_node_value(node: int, value: int):
    tree[node][0] = value
    tree[node][1] = True


def dirty(node: int):
    if tree[node] is None:
        return True

    return tree[node][1] == False


# set all leaf nodes to 0
for i in range(1, 2 ** (tree_height - 1) + 1):
    update(i, 0)

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
