import sys
input = lambda: sys.stdin.readline().rstrip() # 속도 최적화 (효과있나?)

C = int(input())

memo = dict()

results = []

for _ in range(C):
    memo.clear()

    a, b = tuple(map(int, input().split()))

    numA = [0] + list(map(int, input().split()))
    numB = [0] + list(map(int, input().split()))

    def solve(indexA, indexB): # int, int -> int
        if indexA > a or indexB > b:
            return 0

        if (indexA, indexB) not in memo:
            valA = numA[indexA]
            valB = numB[indexB]
    
            result = 0
    
            for newIndexA in range(indexA + 1, a + 1):
                newVal = numA[newIndexA]
                if newVal > valA and newVal > valB:
                    result = max(result, solve(newIndexA, indexB))
    
            for newIndexB in range(indexB + 1, b + 1):
                newVal = numB[newIndexB]
                if newVal > valA and newVal > valB:
                    result = max(result, solve(indexA, newIndexB))

            memo[(indexA, indexB)] = result

        return memo[(indexA, indexB)] + 1

    result = 0
    for i in range(-1, a + 1):
        for j in range(-1, b + 1):
            result = max(result, solve(i, j) - 1)

    results.append(str(result))

print('\n'.join(results))

'''
print('--- result ---')

i = 1
for result in results:
    print('result #' + str(i) + ': ' + str(result))
    i += 1
'''