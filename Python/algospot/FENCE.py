import os, sys

C = int(input()) # 테스트 케이스

sys.setrecursionlimit(100000)

results = []

for _ in range(C):
    N = int(sys.stdin.readline()) # 판자 수
    planks = []
    for numStr in sys.stdin.readline().split():
        planks.append(int(numStr))

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