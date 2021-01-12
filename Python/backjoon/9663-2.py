from typing import List


N = int(input())

count = 0

# sol은 어떤 열에 있는지에 대한 설명, n은 높이
def solve(sol: List[int], n: int):
    global count
    if len(sol) == n:
        count += 1
        return

    candidates = [*range(n)]

    for i in range(len(sol)):
        if sol[i] in candidates:
            candidates.remove(sol[i])

        distance = len(sol) - i
        if sol[i] + distance in candidates:
            candidates.remove(sol[i] + distance)

        if sol[i] - distance in candidates:
            candidates.remove(sol[i] - distance)

    if len(candidates) > 0:
        for val in candidates:
            sol.append(val)
            solve(sol, n)
            sol.pop()

for i in range(N):
    solve([i], N)
print(count)