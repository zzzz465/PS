N, K, M = map(int, input().split())

tree_height = 1
while True:
    if 2 ** (tree_height + 1) > N:
        break
    else:
        tree_height += 1