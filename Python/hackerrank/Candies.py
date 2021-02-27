def candies(n, arr):
    memo = dict()
    def getRequiredCandyFor(i):
        nonlocal arr, memo
        
        maxValue = 1
        if i != 0:
            if arr[i] > arr[i-1]:
                maxValue = max(maxValue, getRequiredCandyFor(i-1) + 1)
            
        if i != n-1:
            if arr[i] > arr[i+1]:
                maxValue = max(maxValue, getRequiredCandyFor(i+1) + 1)

        if i not in memo:
            memo[i] = maxValue
        else:
            memo[i] = max(memo[i], maxValue)
        
        return memo[i]

    # 왜 이렇게 해야 하는거지????????
    for i in range(n):
        getRequiredCandyFor(i)

    return sum(memo.values())

print(candies(8, [2,4,3,5,2,6,4,5]))