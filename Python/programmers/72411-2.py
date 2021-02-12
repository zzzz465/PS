from collections import defaultdict, deque
# from itertools import combinations

# 13 14 15 타임아웃 주의
# combinations() 사용하면 13~15 번에서 타임아웃 뜨므로 X

def solution(orders, courses):
    menus = [False] * 26
    max_len = 0

    # for i in range(len(orders)):
    #     orders[i] = ''.join(sorted(orders[i])) # 정렬해서 넣어둠

    for order in orders:
        max_len = max(max_len, len(order))
        for menu in order:
            menus[ord(menu) - ord('A')] = True

    combo_result = defaultdict(list)
    possible_combos = deque([chr(i + ord('A')) for i in filter(lambda key: menus[key], range(26))])

    while len(possible_combos) > 0:

        for _ in range(len(possible_combos)): # 가능한 경우의 수 모두 도출해낸 다음
            combo = possible_combos.popleft()
            last = combo[-1:]
            for i in range(26):
                if ord(last) - ord('A') < i and menus[i]:
                    newCombo = combo + chr(i + ord('A'))
                    possible_combos.append(newCombo)

        combo_counter = defaultdict(list)
        for _ in range(len(possible_combos)):
            combo = possible_combos.popleft()
            count = 0
            for order in orders:
                if all(map(lambda c: c in order, combo)):
                    count += 1

            if count >= 2: # 2명 이상에게서 발견된 조합만 꺼냄
                combo_counter[count].append(combo)
                possible_combos.append(combo)

        if len(combo_counter) > 0:
            max_key = max(combo_counter.keys())

            if max_key >= 2:
                max_combos = combo_counter[max_key]
                combo_result[len(max_combos[0])] = max_combos

    result = []

    for combo_count in courses:
        if combo_count in combo_result:
            result.append(combo_result[combo_count])

    return sorted(sum(result, []))

if __name__ == '__main__':
    res1 = solution(['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH'], [2, 3, 4])

    exit(0)