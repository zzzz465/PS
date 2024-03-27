from collections import OrderedDict


class Node:
    key: int
    value: int

    left: "Node" | None
    right: "Node" | None

    def max(self):
        if self.right is not None:
            return self.right.max()
        else:
            return self.value

    def search(self, node: "Node"):
        if node.value < self.value:
            if node.left is not None:
                if node.left == node.key:
                    return node.left
                else:
                    node.left.search(node)
        else:
            if node.right is not None:
                if node.right == node.key:
                    return node.right
                else:
                    node.right.search(node)

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
            if node.left is not None:
                if node.left == node.key:
                    node.left = None
                else:
                    node.left.remove(node)
        else:
            if node.right is not None:
                if node.right == node.key:
                    node.right = None
                else:
                    node.right.remove(node)


class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        result = [0] * len(freq)
        idFreq = OrderedDict()

        # tree for searching max value fast
        root = Node()
        root.key = -1
        root.value = -1

        for i in range(len(nums)):
            id = nums[i]
            f = freq[i]

            if id not in idFreq:
                idFreq[id] = 0

            idFreq[id] += f
            idFreq[id] = max(idFreq[id], 0)  # to fix if the value goes negative

            # main cause of time limit error
            maxFreq = max(idFreq.values())
            result[i] = maxFreq

        return result


if __name__ == "__main__":
    assert Solution().mostFrequentIDs([2, 3, 2, 1], [3, 2, -3, 1]) == [3, 3, 2, 2]
    pass
