# from collections import deque
import sys

queue = list()
minstr = ''

def solution(s: str):
    global minstr

    if s == '':
        stringify = ''
        for string, count in queue:
            if count > 1:
                stringify += f'{count}{string}'
            else:
                stringify += f'{string}'

        if minstr == '' or len(stringify) < len(minstr):
            minstr = stringify
        return

    for i in range(1, len(s) + 1):
        chunk = [s[:i], 1]
        queue.append(chunk)

        nextIndex = i

        for j in range(i, len(s) + 1, i):
            if s[j:j+i] == chunk[0]:
                chunk[1] += 1
                nextIndex = j + i
            else:
                break

        solution(s[nextIndex:])

        queue.pop()

    pass

solution('aabbaccc')
print(len(minstr))