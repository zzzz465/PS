import os, sys

C = int(input()) # 테스트 케이스

sys.setrecursionlimit(100000)

for _ in range(C):
    N = int(input()) # 판자 수
    planks = list(map(int, input().split())) # 판자 개수는 1~10000개, 각각의 높이 범위는 1~10000개 이다

    def getMax(start, end): # start: int, end: int
        # start과 end는 index, 0 ~ len(planks) - 1
        if start == end:
            return planks[start]

        mid = int((start + end) / 2)

        max_left = getMax(start, mid) # 왼쪽에 있을 경우
        max_right = getMax(mid + 1, end) # 오른쪽에 있을 경우

        max_size = max(max_left, max_right)

        low = mid
        high = mid + 1
        height = min(planks[low:high + 1])

        max_size = max(max_size, height * 2)

        while start < low or high < end:
            if high < end and (low == start or planks[low - 1] < planks[high + 1]):
                high += 1
                height = min(height, planks[high])
            else:
                low -= 1
                height = min(height, planks[low])

            max_size = max(max_size, height * (high - low + 1))

        return max_size

    max_size = getMax(0, len(planks) - 1)

    print(max_size)