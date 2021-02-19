def pairs(k, arr):
    counter = set(arr)

    keys = sorted(list(counter))

    totalCount = 0
    for key in keys:
        other = k + key
        if other in counter:
            totalCount += 1

    return totalCount
