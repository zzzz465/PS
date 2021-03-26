N = int(input())
line = input()

cache = dict()
def solve(index: int):
    if index < 0 or line[index] == '0':
        return 0

    if index == 0:
        return 1

    if index not in cache:
        res = solve(index - 1) + solve(index - 2)
        cache[index] = res

    return cache[index]

print(solve(N-1))