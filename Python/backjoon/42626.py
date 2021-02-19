import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    totalMixCount = 0
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        newFood = first + second * 2
        totalMixCount += 1
        heapq.heappush(scoville, newFood)

    return totalMixCount

solution([1, 2, 3, 9, 10, 12], 7)