'''
모듈러 연산에 잘 알아야 함
https://en.wikipedia.org/wiki/Modular_arithmetic
(a+b)%M=(a%M+b%M)%M
(a−b)%M=(a%M−b%M)%M
'''

### pypy3

# Enter your code here. Read input from STDIN. Print output to STDOUT
import bisect

def maximumSum(a, m):
    maxModulo = -1
    a[0] %= m
    for i in range(1, len(a)):
        a[i] = (a[i-1] + a[i]) % m
        
    maxModulo = a[0] % m
    memo = [a[0]]
        
    for i in range(1, len(a)):
        maxModulo = max(maxModulo, a[i])
        
        index = bisect.bisect_left(memo, a[i] + 1)
        if index < len(memo):
            maxModulo = max(maxModulo, (a[i] - memo[index]) % m)

        bisect.insort(memo, a[i])
    
    return maxModulo

C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    print(maximumSum(a, m))
