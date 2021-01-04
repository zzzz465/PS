import os, sys

C = int(input()) # 테스트 케이스

results = []

for _ in range(C):
    N = int(input()) # 판자 수
    planks = list(map(int, input().split())) # 판자 개수는 1~10000개, 각각의 높이 범위는 1~10000개 이다

    def solve(left, right):
        global planks
        if left == right: return planks[left]

        mid = int((left + right) / 2)

        ret = max(solve(left, mid), solve(mid + 1, right))

        low = mid; high = mid + 1
        height = min(planks[low], planks[high])

        ret = max(ret, height * 2)
        
        while left < low or high < right:
            if high < right and (low == left or planks[low - 1] < planks[high + 1]):
                high += 1
                height = min(height, planks[high])
            else:
                low -= 1
                height = min(height, planks[low])
        
            ret = max(ret, height * (high - low + 1))

        return ret

    max_size = solve(0, N - 1)

    results.append(str(max_size))

print('\n'.join(results))