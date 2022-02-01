N, K, M = map(int, input().split())

tree_height = 1
while True:
    if 2 ** (tree_height + 1) > N:
        break
    else:
        tree_height += 1

tree_nodes_count = 2 ** (tree_height) + 1  # starts from 1

tree = [0] * tree_nodes_count


def update(start: int, end: int, node: int, index: int, value: int):
    if start == end:
        tree[node] = value

    mid = (start + end) // 2

    if mid <= index:
        return update(start, mid, node * 2, index, value)
    else:
        return update(mid + 1, end, node * 2 + 1, index, value)


def query(start: int, end: int, node: int, range_start: int, range_end: int):
    if start == range_start and end == range_end:
        return tree[node]

    mid = (start + end) // 2

    left = query(start, mid, node * 2, range_start, mid)
    right = query(mid + 1, end, node * 2 + 1, mid + 1, end)

    return left + right
