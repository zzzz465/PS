import sys

def maxMin(k, arr):
    arr.sort()

    i = 0
    j = k - 1
    minFairness = sys.maxsize
    while j < len(arr): # conditions?
        absDelta = abs(arr[j] - arr[i])
        minFairness = min(minFairness, absDelta)

        i += 1
        j += 1

    return minFairness

