from typing import Dict, List

clothes = dict()
types = list()
count = 0

def solve():
    result = 1

    for type in types:
        count = len(clothes[type])
        result *= (count + 1)

    return result - 1

''' # 재귀버전
def solve(index: int, clothCount: int):
    global clothes, types, count

    if index >= len(types):
        if clothCount > 0:
            count += 1

        return

    for i in range(len(clothes[types[index]])):
        solve(index + 1, clothCount + 1) # 선택

    solve(index + 1, clothCount) # 미선택
'''


def solution(clothList: List[List[str]]):
    global clothes, types, count

    for cloth in clothList:
        if cloth[1] not in clothes:
            clothes[cloth[1]] = list()

        clothes[cloth[1]].append(cloth[0])

    types = [*clothes.keys()]

    # solve(0, 0) # 재귀
    # return count

    return solve()


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
# print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))