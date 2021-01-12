
C = int(input())
memo = dict()

for _ in range(C):
    N = int(input())
    numbers = list(map(int, input().split()))
    memo.clear()

    def solve(index): # int -> int (길이)
        if index >= N:
            return 0

        if index not in memo:
            val = numbers[index]
            result = 0
            for newIndex in range(index + 1, N):
                if numbers[newIndex] > val:
                    result = max(result, solve(newIndex))

            memo[index] = result

        return memo[index] + 1

    result = 0
    for i in range(N):
        result = max(result, solve(i))

    print(result)
