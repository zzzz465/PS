N, K, M = map(int, input().split())

leaf_nodes_count = 1
tree_height = 1
while leaf_nodes_count < N:
    leaf_nodes_count *= 2
    tree_height += 1

tree_nodes_count = 2 ** (tree_height) - 1


tree = [0] * (tree_nodes_count + 1)


def update(start: int, end: int, node: int, index: int, value: int):
    if start == end:
        tree[node] = value
        return value

    mid = (start + end) // 2

    left, right = 0, 0

    if index <= mid:
        left = update(start, mid, node * 2, index, value)
        right = query(mid + 1, end, node * 2 + 1, mid + 1, end)
        tree[node] = left + right
    else:
        left = query(start, mid, node * 2, start, mid)
        right = update(mid + 1, end, node * 2 + 1, index, value)
        tree[node] = left + right

    return left + right


def query(start: int, end: int, node: int, range_start: int, range_end: int):
    if end < range_start or start > range_end:
        return 0

    if start == range_start and end == range_end:
        return tree[node]

    mid = (start + end) // 2

    if range_start <= mid <= range_end:
        left = query(start, mid, node * 2, range_start, mid)
        right = query(mid + 1, end, node * 2 + 1, mid + 1, end)
    else:
        left = query(start, mid, node * 2, range_start, range_end)
        right = query(mid + 1, end, node * 2 + 1, range_end, range_end)

    return left + right


for i in range(1, N + 1):
    val = int(input())
    update(1, leaf_nodes_count, 1, i, val)


for _ in range(K + M):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, leaf_nodes_count, 1, b, c)
    else:
        res = query(1, leaf_nodes_count, 1, b, c)
        print(res)

'''
test cases

#1
5 1 2
1
2
3
4
5
2 5 5
1 1 5
2 5 5

A: ?

#2
5 0 1
1
2
6
4
2
2 1 4

A: 13

#3
5 1 1
1
2
3
4
5
1 1 6
2 4 5

A: 9
'''
