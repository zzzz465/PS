C = int(input()) # 테스트 케이스

# 아이디어
'''
N개의 판자 중에서 가장 큰 사각형을 구하는 방법은
N-1 개의 판자 중에서 가장 큰 사각형과 N개의 판자를 사각형으로 만들었을 때
더 큰 것을 선택하면 된다.
N-1개의 판자보다 N개의 판자로 만드는 사각형이 더 크다면, N-2보다는 당연히 더 커질 것이므로
'''

for _ in range(C):
    N = int(input()) # 판자 수
    planks = list(map(int, input().split())) # 판자 개수는 1~10000개, 각각의 높이 범위는 1~10000개 이다

    def getMax(start, end): # start: int, end: int
        if start < end:
            length = end - start

            if length == 1: # 기저 사례: 더이상 쪼갤 수 없으므로 판자 그 자체가 하나의 사각형임
                return planks[start]

            max_1 = min(planks[start:start + length]) * length
            max_2 = getMax(start, end - 1)
            max_3 = getMax(start + 1, end)

            return max(max_1, max_2, max_3)
        else:
            return 0

    max_size = getMax(0, len(planks))

    print(max_size)
