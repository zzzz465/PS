from collections import Counter, defaultdict
from itertools import combinations, chain

def solution(orders, courses):
    counter = Counter()
    for order in orders:
        for menu in order:
            counter[menu] += 1

    memo = defaultdict(list)
    for menu, count in counter.most_common():
        memo[count].append(menu)

    keys = [*memo.keys()]

    result = []

    for menu_count in courses:
        candidates = sum([memo[key] for key in filter(lambda x: x >= menu_count, keys)], [])
        for combo in combinations(candidates, menu_count):
            count = 0
            for order in orders:
                if all(map(lambda x: x in order, combo)):
                    count += 1

            if count > 2:
                if combo not in result:
                    result.append(combo)
                    break

    result.sort()

    return result

if __name__ == '__main__':
    res1 = solution(['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH'], [2, 3, 4])

    exit(0)