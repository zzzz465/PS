from collections import deque
# li 라는 배열을, start index 부터 end index 까지 reverse
def reverse(li, start, end):
    lo = start
    hi = end
    while (lo < hi):
        temp = li[hi]
        li[hi] = li[lo]
        li[lo] = temp
        lo += 1; hi -= 1

memo = dict()

def preCalculate(n): # int -> void
    initial = tuple([i for i in range(1, n + 1)])

    queue = deque([[0, initial]])

    while len(queue) > 0:
        curr = queue.popleft()
        
        if curr[1] in memo:
            continue
        else:
            memo[curr[1]] = curr[0]

        li = list(curr[1])
        for i in range(0, n):
            for j in range(i+1, n):
                if i != j:
                    reverse(li, i, j)
                    queue.append([curr[0] + 1, tuple(li)])
                    reverse(li, i, j)

def normalizeNumbers(li):
    result = []
    for i in range(len(li)):
        greaterCount = 1
        for j in range(len(li)):
            if li[i] > li[j]:
                greaterCount += 1
        
        result.append(greaterCount)

    return result

# main
C = int(input())

for i in range(C):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = normalizeNumbers(numbers)

    preCalculate(N)
    print(memo[tuple(numbers)])