n, k = map(int, input().split())

weightsSet = set()

for i in range(n):
    weightsSet.add(int(input()))

# :mollu:
weights = sorted(weightsSet)
weightsReversed = weights[::-1]

# bottom-up?
maxVal = 100000000
memo = [maxVal] * 100001
sol = maxVal

def solve(value: int) -> int:
    global weightsReversed, memo, maxVal, k

    for other in weightsReversed:
        newValue = value + other

        if newValue > k:
            continue
        elif newValue == k:
            return 1

        computed = solve(newValue) + 1

        if computed > sol:
            return maxVal
        
        memo[value] = min(memo[value], computed)

    return memo[value]


for w in weightsReversed:
    computed = solve(w)
    sol = min(sol, computed)

if sol != maxVal:
    print(sol)
else:
    print(-1)
