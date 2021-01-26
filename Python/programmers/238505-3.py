from collections import deque
from queue import Queue

def solution(operations):
    root = None

    priority_queue = deque()

    for opcode, operand in map(lambda x: x.split(), operations):
        if opcode == 'I':
            operand = int(operand)
            stack = list()
            while len(priority_queue) > 0:
                front = priority_queue.popleft()
                if front > operand:
                    stack.append(front)
                else:
                    priority_queue.appendleft(front)
                    break
            priority_queue.appendleft(operand)
            while len(stack) > 0:
                top = stack.pop()
                priority_queue.appendleft(top)
        
        else:
            if operand == '1':
                if len(priority_queue) > 0:
                    priority_queue.popleft()
            else:
                if len(priority_queue) > 0:
                    priority_queue.pop()

    if len(priority_queue) > 0:
        return [max(priority_queue), min(priority_queue)]
    else:
        return [0, 0]

if __name__ == '__main__':
    res1 = solution(['I 16', 'D 1'])
    res2 = solution(['I 7', 'I 5', 'I -5', 'D -1'])

    exit(0)