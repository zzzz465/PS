import sys
N = int(input())

minVal = sys.maxsize
numbers = [0] * N
for i in range(N):
    numbers[i] = int(input())
    minVal = min(minVal, numbers[i])
    
res = []

for i in range(2, minVal + 1):
    reminders = map(lambda x: x % i, numbers)
    if len(set(reminders)) == 1:
        res.append(i)

print(' '.join(map(str, res)))