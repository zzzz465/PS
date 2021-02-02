N = int(input())

numbers = sorted([*map(int, input().split())])

lo = 0
hi = len(numbers) - 1

minLow = 0
maxHigh = hi

delta = abs(numbers[hi] + numbers[lo])

while lo < hi:
    val = numbers[hi] + numbers[lo]

    if abs(val) >= delta:
        if val > 0:
            hi -= 1
        else:
            lo += 1
    else:
        minLow = lo
        maxHigh = hi
        delta = abs(val)

result = (numbers[minLow], numbers[maxHigh])

# print(result)
print(f'{result[0]} {result[1]}')