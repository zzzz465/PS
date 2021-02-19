import bisect

def triplets(a, b, c):
    # need?
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    count = 0
    for bVal in b:
        aIndex = bisect.bisect_right(a, bVal)
        cIndex = bisect.bisect_right(c, bVal)
        count += aIndex * cIndex

    return count