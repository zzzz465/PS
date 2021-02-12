
from typing import List


def solution(answers: List[int]):
    count = [0, 0, 0]

    sol1 = [1, 2, 3, 4, 5]
    sol2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sol3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == sol1[i % 5]:
            count[0] += 1

        if answers[i] == sol2[i % 8]:
            count[1] += 1

        if answers[i] == sol3[i % 10]:
            count[2] += 1

    maxVal = max(count)
    res = []

    for i in range(len(count)):
        if count[i] == maxVal:
            res.append(i + 1)

    return res