import bisect
from collections import defaultdict
from typing import Dict

def compare(item1, item2):
    for i in range(4):
        if item1[i] != item2[i]:
            if item1[i] < item2[i]:
                return -1
            else:
                return 1

    return item1[4] - item2[4]

def convert(text):
    li = text.split(' ')
    li[len(li) - 1] = int(li[len(li) - 1])
    return li

def convert_query(text):
    li = [*map(lambda x: x.strip(), text.split(' '))] # 텍스트 파싱
    li = [*filter(lambda x: x != 'and', li)]
    li[len(li) - 1] = int(li[-1])

    return li

def make_table(li, start, end, depth, max_depth):
    if depth == max_depth:
        return { 'start': start, 'end': end, 'depth': depth }

    d = defaultdict()
    index = start
    token = li[start][depth]
    while index <= end:
        if li[index][depth] != token:
            # end is here
            sub = make_table(li, start, index - 1, depth + 1, max_depth)
            d[token] = { 'start': start, 'end': index - 1, 'sub': sub, 'depth': depth }
            start = index
            token = li[start][depth]
        else:
            index += 1

    if index - start > 0:
        sub = make_table(li, start, index - 1, depth + 1, max_depth)
        d[token] = { 'start': start, 'end': index - 1, 'sub': sub, 'depth': depth }

    return d

def binary_search(li, start, end, value):
    candidates = [*map(lambda x: x[4], li[start:end+1])]
    index = bisect.bisect_left(candidates, value)
    if index == len(candidates):
        return 0
    elif candidates[index] >= value:
        return len(candidates) - index
    else:
        return len(candidates) - index - 1

def find(li, table: Dict, query):
    count = 0

    if len(query) == 1: # 마지막
        count = binary_search(li, table['start'], table['end'], query[0])

    elif query[0] == '-':
        for value in table.values():
            count += find(li, value['sub'], query[1:])
    
    else:
        if query[0] in table:
            obj = table[query[0]]
            sub = obj['sub']
            count = find(li, sub, query[1:])

    return count

def solution(info, queries):
    li = [*map(convert, info)]

    li.sort()

    table = make_table(li, 0, len(li) - 1, 0, 4) # 0 1 2 3 4 depth (5개)

    result = []

    for query in queries:
        query = convert_query(query)
        result.append( find(li, table, query) )

    return result


if __name__ == '__main__':
    info1 = [
        'java backend junior pizza 150',
        'python frontend senior chicken 210',
        'python frontend senior chicken 150',
        'cpp backend senior pizza 260',
        'java backend junior chicken 80',
        'python backend senior chicken 50'
    ]
    query1 = [
        'java and backend and junior and pizza 100',
        'python and frontend and senior and chicken 200',
        'cpp and - and senior and pizza 250',
        '- and backend and senior and - 150',
        '- and - and - and chicken 100',
        '- and - and - and - 150'
    ]

    result = solution(info1, query1)
    pass
