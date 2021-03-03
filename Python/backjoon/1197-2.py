import sys
from typing import List, Set

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.connected = set()

def isConnected(a: Node, b: Node):
    def _DFS(root: Node, target: Node, memo: Set[Node]) -> bool:
        if root == target:
            return True

        if root in memo:
            return False
        else:
            memo.add(root)

        for other in root.connected:
            connected = _DFS(other, target, memo)
            if connected:
                return True

        return False
    
    return _DFS(a, b, set())

def connect(a: Node, b: Node):
    a.connected.add(b)
    b.connected.add(a)

def solve():
    V, E = map(int, sys.stdin.readline().rstrip().split())

    # create nodes
    nodes = [None] + [Node(i) for i in range(1, V + 1)]

    # add edges into heapq?? why not just use sort?
    edges = [None] * E
    for i in range(E):
        a, b, w = map(int, sys.stdin.readline().rstrip().split())
        edges[i] = (w, a, b)
        # heapq.heappush(edges, (w, a, b))

    edges.sort(key=lambda x: x[0])

    # iterate edge
    # if not connected
    # connect and collect weight
    totalWeight = 0
    connectedEdges = 1
    for edge in edges:
        weight, a, b = edge
        if not isConnected(nodes[a], nodes[b]):
            connect(nodes[a], nodes[b])
            totalWeight += weight
            connectedEdges += 1

        if connectedEdges == V:
            break

    # return total weight
    return totalWeight

print(solve())
