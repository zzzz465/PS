import heapq
from sys import maxsize

NaN = maxsize

def solve():
    V, E, n, m = map(int, input().split())

    matrix = [[0] * (V+1) for _ in range((V+1))]

    for _ in range(E):
        a, b, t = map(int, input().split())
        matrix[a][b] = t
        matrix[b][a] = t
    
    burningHouses = list(map(int, input().split()))
    fireHouses = list(map(int, input().split()))
    
    weights = [NaN] * (V+1)

    pq = list(map(lambda p: (0, p), fireHouses))
    
    for i in fireHouses: # start from firehouse
        weights[i] = 0

    while len(pq) > 0:
        curr_d, curr_p = heapq.heappop(pq)

        if curr_d > weights[curr_p]:
            continue

        for there in range(V+1):
            if matrix[curr_p][there] > 0:
                nextDist = curr_d + matrix[curr_p][there]
                if nextDist < weights[there]:
                    weights[there] = nextDist
                    heapq.heappush(pq, (weights[there], there))
        
    print(sum(map(lambda x: weights[x], burningHouses)))

C = int(input())

for _ in range(C):
    solve()