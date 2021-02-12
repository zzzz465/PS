#
from typing import List, Set


li: List[int]

memo = list()

def solve(index: int):
    if index < 1:
        return [set(), 0]

    for otherIndex in range(index - 1, -1, -1):
        common, length = solve(otherIndex - 1)
        if li[index] in common or li[otherIndex] in common:
            return [common, length + 2]
        else:
            return [set([li[index], li[otherIndex]]), 2]

    return solve(index - 1)

def solution(a):
    global li
    li = a

    max_val = 0
    for index in range(len(a) - 1, -1, -1):
        max_val = max(max_val, solve(index)[1])

    return max_val

    # return solve(len(a) - 1)


if __name__ == '__main__':
    zero = solution([0])
    four = solution([5, 2, 3, 3, 5, 3])
    eight = solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0])

    exit(0)