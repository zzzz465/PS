
from typing import List


def solution(citations: List[int]):
    citations.sort()

    hMax = 0

    for i in range(len(citations)):
        h = citations[i]
        left = i + 1
        right = len(citations) - i

        if left <= h and right >= h:
            hMax = h if h > hMax else hMax

    return hMax