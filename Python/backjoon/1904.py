N = int(input())

# 이거 못푸는게 실화냐?

memo = [1, 2]

for _ in range(N - 1):
    val = memo[0] + memo[1]
    memo[0] = memo[1]
    memo[1] = val % 15746

print(memo[0])