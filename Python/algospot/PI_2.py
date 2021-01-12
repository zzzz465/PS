import sys
sys.setrecursionlimit(100000)

INF = 987654321
text = ''

def classify(start, end):
    if text[start:end + 1] == text[start] * (end - start + 1):
        return 1

    progressive = True
    for i in range(end - start - 1):
        if int(text[i + 1]) - int(text[i]) != int(text[1]) - int(text[0]):
            progressive = False
            break

    if progressive and abs(int(text[1]) - int(text[0])) == 1:
        return 2

    alternating = True
    for i in range(len(text)):
        if text[i] != text[i % 2]:
            alternating = False
            break

    if alternating:
        return 4
    if progressive:
        return 5

    return 10

memo = dict()

def memorize(begin):
    if begin not in memo:
        result = INF
        for i in range(3, 5 + 1):
            if i + begin <= len()
            result = min(result, memorize())
    pass

N = int(input())

for _ in range(N):
    inputText = input()


