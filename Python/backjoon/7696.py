
from typing import List

cache = [False] * 10000000
def calculate(texts: List[int]):
    if len(texts) >= 7:
        return
    
    for i in range(10):
        if i not in texts:
            texts.append(i)
            casted = int(''.join(map(str, texts)))
            cache[int(''.join(map(str, texts)))] = True
            calculate(texts)
            texts.pop()

def find(n):
    count = 0
    for i in range(1, 1000001):
        if cache[i]:
            count += 1
        
        if count == n:
            return i

calculate([])

while True:
    value = int(input())
    if value != 0:
        print(find(value))
    else:
        exit(0)
