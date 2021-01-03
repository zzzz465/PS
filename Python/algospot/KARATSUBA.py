def multiply(a, b): # a: List[int], b: List[int] -> List[int]
    pass

def add(a, b): # a: List[int], b: List[int] -> List[int]
    # 길이 a < b
    if len(a) <= len(b):
        result = list()
        for i in range(len(a)): # a와 b 공통된 부분을 더하고
            result.append(a[i] + b[i])

        return normalize(result + b[len(a):])km # b의 나머지 부분을 뒤에 붙여서 반환
    else:
        add(b, a)

def normalize(li): # li: List[int] -> List[int]
    result = list()
    for i in range(len(li)):
        val = li[i]
        if len(result) == i: # index 할당 X
            if val >= 10:
                result.append(val % 10)
                result.append(val / 10)
            else:
                result.append(val)
        else: # index 할당 됨, 뒤에 자리가 할당되었는지는 모름
            result[i] += val
            if len(result) + 1 > i: # 뒷 자리도 할당되었을 경우
                result[i + 1] += result[i] / 10
            else: # 뒷 자리 할당 X 일 경우
                result.append(result[i] / 10)

            result[i] %= 10

    return result

def subFrom(a, b): # a >= b 일때 a - b 를 구현
    if len(a) >= len(b):
        result = list()
        for i in range(len(b)):

    else:
        subFrom(b, a)

def karatsuba(a, b): # a: List[int], b: List[int] -> List[int]
    if len(a) < len(b):
        karatsuba(b, a)

    if len(a) == 0 or len(b) == 0:
        return []

    if len(a) <= 50:
        return multiply(a, b)

    half = int(len(a) / 2)

    a0 = a[0:half]
    a1 = a[half:]
    b0 = b[0:half]
    b1 = b[half:]

    z0 = karatsuba(a0, b0)
    z2 = karatsuba(a1, b1)
    z1 = subFrom(subFrom( multiply(multiply(a0, a1), multiply(b0, b1)), z0), z2) # (a0 + a1) * (b0 + b1) - z0 - z2

    return add(add(z0, z1), z2)