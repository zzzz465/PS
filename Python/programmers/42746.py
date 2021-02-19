from functools import cmp_to_key

def compare(x: str, y: str):
    down = int(x + y)
    up = int(y + x)
    if down < up:
        return 1

    elif down > up:
        return -1

    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))

    return str(int(''.join(numbers)))

solution([3, 30, 34, 5, 9])
