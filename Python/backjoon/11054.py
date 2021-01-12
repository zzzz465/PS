import sys
sys.setrecursionlimit(10000)

N = int(input())
numbers = [*map(int, input().split())]

first_check_memo = dict()
second_check_memo = dict()

def first_check(number: int, index: int) -> int:
    if index < 0:
        return 0

    if (number, index) not in first_check_memo:
        result = first_check(number, index - 1) # 스킵했을 경우

        if numbers[index] < number:
            result = max(result, first_check(numbers[index], index - 1) + 1)

        first_check_memo[(number, index)] = result

    return first_check_memo[(number, index)]

def second_check(number: int, index: int) -> int:
    if index >= N:
        return 0

    if (number, index) not in second_check_memo:
        result = second_check(number, index + 1) # 스킵했을 경우

        if numbers[index] < number:
            result = max(result, second_check(numbers[index], index + 1) + 1)

        second_check_memo[(number, index)] = result

    return second_check_memo[(number, index)]

max_len = 0

for i in range(N):
    first = first_check(numbers[i], i)
    second = second_check(numbers[i], i)
    length = first + second + 1

    if max_len < length:
        max_len = length

print(max_len)
