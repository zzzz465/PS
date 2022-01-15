
from typing import Dict, List


n, k = map(int, input().split())

weights: List[int] = [0] * n
weightsTable: Dict[int, int] = dict()
memo: List[List[int]] = [-1] * 100001
maxVal = 100000000
# value == -1 -> not exist
# value == 0 -> not observed yet

# 2-depth 배열, <key, optimizedValue>

for index in range(n):
    value = int(input())
    weights[index] = value
    memo[value] = maxVal
    weightsTable[value] = index

def getMinimum(value: int) -> int:
    other = n - value

    if memo[other] == -1:
        return maxVal

    if other == 0:
        return 1

    otherIndex = weightsTable[other]
    for i in range(otherIndex - 1):
        computed = getMinimum(weights[i])
        
        memo[value] = min(memo[value], computed)

    return memo[value]

    # 값 존재 X -> 건너뜀
    # 값 존재 O -> 재귀적으로 해당 값의 minimum 계산
    # 계산 -> 자신 index - 1 부터 0 까지 재귀적으로 순회하면서 참조
    # min 값을 만날 경우 값 갱신s
    # 마지막에 아무것도 선택 안하고 자기만 선택하는 경우도 고려
    # 마지막에 갱신된 값 할당?

sol = maxVal

for i in range(n)[::-1]:
    computed = getMinimum(weights[i])
    sol = min(sol, computed)

print(sol)
