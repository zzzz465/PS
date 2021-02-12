import sys

sys.setrecursionlimit(10**5 + 1000)

from typing import List

N = int(input())

infixes = [*map(int, input().split())]
postfixes = [*map(int, input().split())]

def find(li: List[int], start: int, end: int, value: int):
    for index in range(start, end + 1):
        if li[index] == value:
            return index

    return -1 # ?

# postfixIndex는 현재 head가 어딘지 가리킴
def solve(infixStart: int, infixEnd: int, postfixHeadIndex: int):
    if infixStart > infixEnd:
        return

    head = postfixes[postfixHeadIndex]
    infixHeadIndex = find(infixes, infixStart, infixEnd, head)
    
    leftInfixStart = infixStart
    leftInfixEnd = infixHeadIndex - 1

    rightInfixStart = infixHeadIndex + 1
    rightInfixEnd = infixEnd

    print(head, end=' ')

    # postfix head index
    rightPostfixHeadIndex = postfixHeadIndex - 1
    leftPostfixHeadIndex = postfixHeadIndex - (rightInfixEnd - rightInfixStart + 1) - 1

    solve(leftInfixStart, leftInfixEnd, leftPostfixHeadIndex)
    solve(rightInfixStart, rightInfixEnd, rightPostfixHeadIndex)

solve(0, len(infixes) - 1, len(postfixes) - 1)
