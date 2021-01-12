INF = 987654321

def trinomial(predicate, val1, val2):
    if predicate:
        return val1
    else:
        return val2

def solve(numbers, s): # 정렬된 숫자 배열
    pSum = [numbers[0]] * len(numbers)
    pSqSum = [numbers[0] * numbers[0]] * len(numbers)

    for i in range(1, len(numbers)):
        pSum[i] = pSum[i - 1] + numbers[i]
        pSqSum[i] = pSqSum[i-1] + numbers[i] * numbers[i]

    def minError(low, high):
        nonlocal pSum, pSqSum
        sumVal = pSum[high] - trinomial(low == 0, 0, pSum[low-1])
        sqSumVal = pSqSum[high] - trinomial(low == 0, 0, pSqSum[low-1])
        m = int(0.5 + sumVal / (high - low + 1))

        result = sqSumVal - 2 * m * sumVal + m * m * (high - low + 1)
        return result

    memo = dict()
    def quantize(index, parts):
        nonlocal pSum, pSqSum
        if index == len(numbers): # 기저사례: 모든 숫자를 양자화 했을 때
            return 0
        if parts == 0: # 숫자가 남았는데 더 묶을 수 없을 경우
            return INF

        if (index, parts) not in memo:
            result = INF
            for newIndex in range(index, len(numbers)):
                result = min(result, minError(index, newIndex) + quantize(newIndex + 1, parts - 1))

            memo[(index, parts)] = result

        return memo[(index, parts)]

    result = quantize(0, s)

    return result

C = int(input())

for _ in range(C):
    N, S = tuple(map(int, input().split())) # N개의 길이의 숫자 배열이 들어오고, S 개로 양자화

    numbers = sorted(list(map(int, input().split()))) # 길이 N
    # K 개의 숫자 그룹이 있다, 이것을 S 개의 숫자로 표준화 시켜야함
    
    print(solve(numbers, S))

