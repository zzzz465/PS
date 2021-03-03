
V, E = map(int, input().split())

roots = [i for i in range(V + 1)]
def root(index: int):
    if roots[index] == index:
        return index
    else:
        otherHead = root(roots[index])
        roots[index] = otherHead
        return otherHead

def union(a: int, b: int):
    if root(a) != root(b):
        roots[b] = a

edges = [None] * E
for i in range(E):
    a, b, w = map(int, input().split())
    edges[i] = (a, b, w)

edges.sort(key=lambda x: x[2])

vertex_count = 0
weightSum = 0
for edge in edges:
    a, b, w = edge
    if root(a) != root(b):
        union(a, b)
        weightSum += w
        vertex_count += 1

    if vertex_count == V-1:
        break

print(weightSum)