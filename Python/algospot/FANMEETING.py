import sys

C = int(input())

# 남 x 남만 문제되는것
# 여 x 여, 여 x 남, 남 x 여 는 상관없음
# 뒤에서부터 검사하는게 좋은 방법

answers = ''

for _ in range(C): # 문자열 매칭 문제
    MEMBERS = list(sys.stdin.readline().rstrip())
    FANS = list(sys.stdin.readline().rstrip())

    jumps = [None] * len(MEMBERS)

    for i in range(len(MEMBERS) - 1, -1, -1): # 역순 접근
        if MEMBERS[i] == 'M':
            offset = 1
            for j in range(i, -1, -1): # i 부터 0까지 검색
                if MEMBERS[j] == 'F':
                    offset = i - j
                    break

            jumps[i] = offset
        else:
            jumps[i] = 1

    # 문제 풀이 단계
    count = 0

    offset = 0
    while True:
        if offset + len(MEMBERS) > len(FANS): # 맴버 배열이 팬보다 뒷쪽으로 밀린경우 -> 더이상 모두가 hug 하는 경우의 수 X
            break

        allHug = True

        for j in range(len(MEMBERS)):
            memberIndex = len(MEMBERS) - 1 - j
            fanIndex = memberIndex + offset

            member = MEMBERS[memberIndex]
            fan = FANS[fanIndex]

            if member == 'M' and fan == 'M':
                offset += jumps[memberIndex]
                allHug = False
                break

        if allHug:
            count += 1
            offset += 1

    answers += (str(count) + '\n')

print(answers.rstrip())