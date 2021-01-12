
C = int(input())

for _ in range(C):
    N = int(input())
    numbers = [*map(int, input().split())]

    numbers.sort()

    count = 0

    while len(numbers) > 1:
        val1 = numbers[0]
        val2 = numbers.pop()
        del numbers[0]

        numbers.append(val1 + val2)
        numbers.sort()
        count += val1 + val2

    print(count)