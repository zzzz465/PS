from collections import deque
import sys
sys.setrecursionlimit

class TreeNode:
    def __init__(self, value, depth):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth

def inorderDFS(root, li):
    if root.left != None:
        inorderDFS(root.left, li)
    
    li.append(root.value)
    
    if root.right != None:
        inorderDFS(root.right, li)

def swapNodes(indexes, queries):
    # 트리 구조 만들기
    root = TreeNode(1, 1)

    q = deque([root])
    for [left, right] in indexes:
        curr = q.popleft()

        if left != -1:
            newNode = TreeNode(left, curr.depth + 1)
            curr.left = newNode
            q.append(newNode)

        if right != -1:
            newNode = TreeNode(right, curr.depth + 1)
            curr.right = newNode
            q.append(newNode)
    
    result = []

    for query in queries:
        q = deque([root])
        while len(q) > 0:
            curr = q.popleft()
            if curr.depth % query == 0: # 배수
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
    
            if curr.left != None:
                q.append(curr.left)

            if curr.right != None:
                q.append(curr.right)

        res = []
        inorderDFS(root, res)
        result.append(res)

    return result

swapNodes([
    [2, 3],
    [4, -1],
    [5, -1],
    [6, -1],
    [7, 8],
    [-1, 9],
    [-1, -1],
    [10, 11],
    [-1, -1],
    [-1, -1],
    [-1, -1]
], [
    2, 2, 4
])