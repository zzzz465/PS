from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Node:
    key: int
    value: int

    left: Union["Node", None]
    right: Union["Node", None]

    def max(self):
        if self.right is not None:
            return self.right.max()
        else:
            return self.value

    def search(self, node: "Node") -> Optional["Node"]:
        if node.value < self.value:
            if node.left is not None:
                if self.left.key == node.key:
                    return node.left
                else:
                    self.left.search(node)
        else:
            if node.right is not None:
                if self.right.key == node.key:
                    return node.right
                else:
                    self.right.search(node)

    def insert(self, node: "Node"):
        if node.value < self.value:
            self.insertLeft(node)
        else:
            self.insertRight(node)

    def insertLeft(self, node: "Node"):
        if self.left is None:
            self.left = node
        else:
            self.left.insert(node)

    def insertRight(self, node: "Node"):
        if self.right is None:
            self.right = node
        else:
            self.right.insert(node)

    def remove(self, node: "Node"):
        if node.value < self.value:
            if self.left is not None:
                if self.left.key == node.key:
                    node.left = None
                else:
                    self.left.remove(node)
        else:
            if self.right is not None:
                if self.right.key == node.key:
                    self.right = None
                else:
                    self.right.remove(node)


class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        result = [0] * len(freq)

        idFreq = defaultdict(int)
        # tree for searching max value fast
        root = Node(-1, -1, None, None)

        for i in range(len(nums)):
            id = nums[i]
            f = freq[i]

            root.remove(Node(id, idFreq[id], None, None))
            idFreq[id] += f
            idFreq[id] = max(idFreq[id], 0)  # to fix negative value
            root.insert(Node(id, idFreq[id], None, None))

            result[i] = root.max()

        return result


if __name__ == "__main__":
    assert Solution().mostFrequentIDs([2, 3, 2, 1], [3, 2, -3, 1]) == [3, 3, 2, 2]
    pass
