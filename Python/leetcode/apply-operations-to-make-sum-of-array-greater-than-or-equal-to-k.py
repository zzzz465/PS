from collections import deque


# typical question using DP + memoization?
class Solution:
    def minOperations(self, k: int) -> int:
        # this might seems hard at first, let's see what we can do
        # 1. bruth-force -> since k <= 10^5, this is clearly not an option
        # 2. greedy -> when [1] and k=11, choosing value that makes sum largest has counterexample
        # when we go with greedy, we'll [1] -> [2] -> [2, 2] -> ... [2, 2, 2, 2, 2, 2] which is 6 step
        # and it's larger than the optimal path, [1] -> [2] -> [3] -> [4] -> [4, 4] -> [4, 4, 4] which is only 5
        # 3. then, we can consider DP (or BFS?)
        # but k can be very, very big, DP will run out of time before reaching the answer
        # in this case, we can use memoization to solve excessive calculations

        # we can compare DFS/BFS depth as step
        # tuple = [sum, step, array]
        queue = deque()
        queue.append((1, 0, (1,)))  # note that , is required for creating tuple

        memo = dict()
        minStep = 987654321

        while len(queue) > 0:
            [sumValue, step, array] = queue.popleft()
            # print("state: ", sumValue, step, array)
            if sumValue >= k:
                minStep = min(minStep, step)
                continue

            # avoid already failed attempts
            if sumValue < k and step >= minStep:
                continue

            maxValue = max(array)

            # copy strategy
            newRecord = (sumValue + maxValue, step + 1, (*array, maxValue))
            # print("copy strategy: ", newRecord)
            if newRecord[2] not in memo or newRecord[1] < memo[newRecord[2]]:
                memo[newRecord[2]] = newRecord[1]
                queue.append(newRecord)

            # increment strategy
            # note that we're storing array is sorted (asc), we can just do this
            newRecord = (sumValue + 1, step + 1, (*array[:-1], maxValue + 1))
            # print("incremental strategy: ", newRecord)
            if newRecord[2] not in memo or newRecord[1] < memo[newRecord[2]]:
                memo[newRecord[2]] = newRecord[1]
                queue.append(newRecord)

        return minStep


if __name__ == "__main__":
    # assert Solution().minOperations(11) == 5
    # assert Solution().minOperations(102)
    # assert Solution().minOperations(98)
    print(Solution().minOperations(95))
    # assert Solution().minOperations(16) == 6
