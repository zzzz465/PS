N = int(input())

memo = dict()

def solve(before: int, left: int) -> int:
    if left == 0:
        return 1

    if (before, left) not in memo:
        result = 0
        if before < 9:
            result += solve(before + 1, left - 1)

        if before > 0:
            result += solve(before - 1, left - 1)

        memo[(before, left)] = result
    
    return memo[(before, left)]

result = 0

for i in range(1, 10):
    result += solve(i, N - 1)

print(result % 1000000000)