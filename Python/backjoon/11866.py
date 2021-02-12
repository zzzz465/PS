from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])

result = []

while len(queue) > 0:
    for i in range(K - 1):
        queue.append(queue.popleft())

    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")