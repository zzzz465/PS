import sys
input = lambda: sys.stdin.readline().rstrip()

C = int(input())

stack = [None] * 2000000
start = 0
end = 0

results = []

for _ in range(C):
    text = input().split()

    if text[0] == 'push':
        stack[end] = text[1]
        end += 1

    elif text[0] == 'front':
        if end - start > 0:
            results.append(stack[start])
        else:
            results.append('-1')

    elif text[0] == 'back':
        if end - start > 0:
            results.append(stack[end-1])
        else:
            results.append('-1')

    elif text[0] == 'size':
        results.append(str(end - start))

    elif text[0] == 'empty':
        if end - start == 0:
            results.append('1')
        else:
            results.append('0')

    elif text[0] == 'pop':
        if end - start > 0:
            results.append(stack[start])
            start += 1
        else:
            results.append('-1')

print('\n'.join(results))