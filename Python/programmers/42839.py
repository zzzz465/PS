from itertools import permutations

def solution(numbers: str):
    possible_numbers = set()
    for i in range(1, len(numbers) + 1):
        for val in map(lambda x: int(''.join(x)), permutations(numbers, i)):
            possible_numbers.add(val)

    max_value = max(possible_numbers)

    sieve = [True] * (max_value + 1) # 에라스토테네스 체
    sieve[0] = False
    sieve[1] = False
    for i in range(2, max_value):
        if i != 2 and i % 2 == 0:
            continue

        j = 2
        while i * j <= max_value:
            sieve[i * j] = False
            j += 1

    count = len(list(filter(lambda x: sieve[x], possible_numbers)))

    return count

solution('17')
solution('011')