def multiply(a, b): # a: List[int], b: List[int] -> List[int]
    result = [0] * (len(a) * len(b) + 1)
    if len(a) >= len(b):
        for i in range(len(a)):
            for j in range(len(b)):
                result[i+j] += a[i] * b[j]

        return normalize(result)
    else:
        multiply(b, a)

def add(a, b): # a: List[int], b: List[int] -> List[int]
    # 길이 a < b
    if len(a) <= len(b):
        result = list()
        for i in range(len(a)): # a와 b 공통된 부분을 더하고
            result.append(a[i] + b[i])

        return normalize(result + b[len(a):]) # b의 나머지 부분을 뒤에 붙여서 반환
    else:
        return add(b, a)

def normalize(li): # li: List[int] -> List[int], li의 요소는 양수만 있다고 가정
    res = list()
    for i in range(len(li)):
        if i < len(res): # 만약 해당하는 index가 이미 있을 경우
            res[i] += li[i]
        else:
            res.append(li[i])

        portion = int(res[i] / 10)
        res[i] %= 10

        if portion > 0:
            if i + 1 < len(res): # 자리 있을경우
                res[i+1] += portion
            else: # 자리 없을경우
                res.append(portion)

    lastIndex = len(res) - 1
    if res[lastIndex] >= 10:
        res.append(int(res[lastIndex] / 10))
        res[lastIndex] %= 10

    while res[len(res) - 1] == 0:
        res.pop()

    return res

def subFrom(a, b): # a >= b을 가정하고 a - b 를 구현
    if len(a) >= len(b):
        pass
    else:
        return subFrom(b, a)

def karatsuba(a, b): # a: List[int], b: List[int] -> List[int]
    if len(a) < len(b):
        return karatsuba(b, a)

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

def karatsubaToString(li):
    return ''.join(list(map(str, list(reversed(li)))))

# tests
assert '500' == karatsubaToString(karatsuba([0, 0, 1], [5]))

bigNumber = [0] * 49 + [1] # 50자리 수, 10^49

assert '1' + '0' * (49 * 2) == karatsubaToString(karatsuba(bigNumber, bigNumber))