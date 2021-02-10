from collections import deque
import sys

sys.setrecursionlimit(10000)

cache = dict()
isCalculated = set()
def preCalculate(n):
    if n in isCalculated:
        return

    queue = deque()
    initial = [i for i in range(0, n)]
    cache[tuple(initial)] = 0
    queue.append(initial) # 초기 값 설정

    while len(queue) > 0:
        front = queue.popleft()
        cost = cache[tuple(front)]
        for i in range(len(front)):
            for j in range(i + 2, len(front) + 1):
                front[i:j+1] = reversed(front[i:j+1])

                t = tuple(front)
                if t not in cache:
                    cache[t] = cost + 1
                    queue.append(list(front))

                front[i:j+1] = reversed(front[i:j+1])
    
    isCalculated.add(n)

def solve():
    N = int(input())
    numbers = list(map(int, input().split()))
    converted = [0] * N

    for i in range(N):
        less = 0
        for j in range(N):
            if numbers[j] < numbers[i]:
                less += 1

        converted[i] = less

    preCalculate(N)
    result = cache[tuple(converted)]
    
    print(result)

C = int(input())

for _ in range(C):
    solve()