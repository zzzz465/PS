import sys
sys.setrecursionlimit(100000)

N = int(input())

numbers = [*map(int, input().split())]

memo = dict()

def solve(number: int, index: int) -> int: # returns length
    if index >= N:
        return 0

    if (number, index) not in memo:
        result = solve(number, index + 1)
        if numbers[index] > number:
            result = max(result, solve(numbers[index], index + 1) + 1)

        memo[(number, index)] = result

    return memo[(number, index)]

print(solve(0, 0))