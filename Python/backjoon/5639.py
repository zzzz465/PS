import sys, os

sys.setrecursionlimit(10*8)

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(head: Node, node: Node):
    if head == None:
        return node

    if node.value < head.value:
        head.left = insert(head.left, node)

    else:
        head.right = insert(head.right, node)

    return head

root = None

while True:
    try:
        num = int(sys.stdin.readline())
        node = Node(num)

        root = insert(root, node)
    except:
        break

def recursive(head: Node):
    if head.left != None:
        recursive(head.left)

    if head.right != None:
        recursive(head.right)

    print(head.value)

recursive(root)