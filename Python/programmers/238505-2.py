priority_queue = list()

def swap(index1, index2):
    temp = priority_queue[index1]
    priority_queue[index1] = priority_queue[index2]
    priority_queue[index2] = temp

def heapifyUp(index):
    if index <= 0:
        return

    parent = int(index / 2)

    if priority_queue[parent] < priority_queue[index]:
        swap(parent, index)
        heapifyUp(parent)

def heapifyDown(index):
    # if index >= len(priority_queue) - 1:
    #     return

    left = index * 2 + 1
    right = index * 2 + 2

    if right < len(priority_queue):
        if priority_queue[right] >= priority_queue[left] and priority_queue[right] > priority_queue[index]:
            swap(index, right)
            heapifyDown(right)
        elif priority_queue[left] > priority_queue[right] and priority_queue[left] > priority_queue[index]:
            swap(index, left)
            heapifyDown(left)

    elif left < len(priority_queue):
        if priority_queue[left] > priority_queue[index]:
            swap(index, left)
            heapifyDown(left)

def insert(value):
    priority_queue.append(value)
    heapifyUp(len(priority_queue) - 1)

def deleteMax():
    if len(priority_queue) > 0:
        swap(0, len(priority_queue) - 1)
        priority_queue.pop()
        heapifyDown(0)

def deleteMin():
    if len(priority_queue) > 0:
        priority_queue.pop()

def solution(operations):
    for opcode, operand in map(lambda x: x.split(), operations):
        if opcode == 'I':
            number = int(operand)
            insert(number)

        else:
            if operand == '1':
                deleteMax()

            else:
                deleteMin()

    if len(priority_queue) == 0:
        return [0, 0]
    else:
        return [max(priority_queue), min(priority_queue)]

if __name__ == '__main__':
    res1 = solution(['I 16', 'D 1'])
    res2 = solution(['I 7', 'I 5', 'I -5', 'D -1'])

    exit(0)