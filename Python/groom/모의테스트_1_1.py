from collections import deque

N, K = map(int, input().split())

nums = [*map(int, input().split())]
minVal = min(nums)

q = deque([(0, tuple(nums))])
cache = dict()
while True:
    count, li = q.popleft() # int, tuple

    if li not in cache:
        cache[li] = count
    else:
        continue

    completed = True
    for i, val in enumerate(li):
        if val == minVal:
            if i > 0 and li[i-1] != minVal and i < N - 1 and nums[i+1] == minVal: # 최적의 위치가 아닐 경우
                continue

            for offset in range(K):
                if not (i-offset >= 0 and i-offset+K <= N): # 부분 배열이 전체 배열의 범위를 벗어날 경우
                    continue

                diff = False
 
                copy_li = list(li)
                for j in range(K):
                    if copy_li[i-offset+j] != minVal:
                        diff = True

                    copy_li[i-offset+j] = minVal

                if diff:
                    q.append([count + 1, tuple(copy_li)])
                    completed = False

    if completed:
        print(count)
        break