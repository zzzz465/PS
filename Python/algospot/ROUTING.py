# 시간초과!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import heapq
from sys import maxsize

NaN = maxsize

def solve():
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]

    for _ in range(M): # get input
        inputStr = input().split()
        a = int(inputStr[0])
        b = int(inputStr[1])
        w = float(inputStr[2])
        matrix[a][b] = w
        matrix[b][a] = w

    # do dijkstra
    # curr = 0 # start = 0, end = n-1
    weights = [NaN] * N
    heap = [(1, 0)] # (dist, position)

    while len(heap) > 0:
        curr_d, curr_p = heapq.heappop(heap)

        if curr_d > weights[curr_p]:
            continue

        for there in range(N):
            if matrix[curr_p][there] > 0:
                nextDist = curr_d * matrix[curr_p][there]
                if nextDist < weights[there]:
                    weights[there] = nextDist
                    heapq.heappush(heap, (weights[there], there))

    print(weights[-1])



# main()
T = int(input())

for _ in range(T):
    solve()