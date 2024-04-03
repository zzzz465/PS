from typing import List

"""
You are given a binary array nums.
We call a subarray alternating if no two adjacent elements in the subarray have the same value.
Return the number of alternating subarrays in nums.

in this problem, we define a new word "subarray alternating"
which means in array, two element adjacents (next to) is not same.
eg. [1, 2, 3] is OK, but [1, 1, 2] is not OK because 1, 1 is same value.

the problem gives us an array of binary values and we need to find alteranting "subarray"
since the given array's length can be 10^5 which is 100000, creating each array is not a good idea (easilly timed out, too many cases)
we need to be clever.


we can make a new boolean array that represents two adjacent value is same or not
(its length will be -1 of original array's length)
then, finding the subarray from it where all values are true will be the subarray alternating.

we can find subarrays by creating a recursing task.
the task will iterate array from given start to end, and if it founds false, makes two subtask that
    runs before and after from found false index
"""


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        isSameValues = [False for _ in range(len(nums) - 1)]

        for i in range(0, len(nums) - 1):
            isSameValues[i] = nums[i] != nums[i + 1]

        def task(start: int, end: int) -> int:
            # guard
            if start >= len(isSameValues):
                return 0

            if start == end:
                if isSameValues[start]:
                    return 1
                else:
                    return 0

            for i in range(start, end):
                if not isSameValues[i]:
                    leftTotal = task(start, i)
                    rightTotal = task(i + 1, end)

                    return leftTotal + rightTotal

            # if no false value is found then we can just nC2 (combination)
            # note that isSameValues is about equality of two adjacent values
            # since we're picking two numbers, not picking two "adjacent" checks
            # we need to add + 1
            n = end - start + 1
            return int(n * (n - 1) / 2)

        result = task(0, len(isSameValues))

        return result + len(nums)


if __name__ == "__main__":
    result1 = Solution().countAlternatingSubarrays([0, 1, 1, 1])
    result2 = Solution().countAlternatingSubarrays([1, 0, 1, 0])

    print("done")
