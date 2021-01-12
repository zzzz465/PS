import sys
sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()

C = int(input())

# 5가지 케이스가 있음

memo = dict()

for _ in range(C):
    line = list(map(int, input()))
    length = len(line)
    memo.clear()

    # 같은 수 반복
    def isSame(start, count): # int, int, int -> bool
        char = line[start]
        for i in range(1, count):
            if line[start + i] != char:
                return False

        return True

    # 단조 증가/감소
    def isMonotonic(start, count):
        flag1 = True; flag2 = True
        for i in range(count - 1):
            if line[start + i + 1] - line[start + i] != 1: # 증가
                flag1 = False

            if line[start + i + 1] - line[start + i] != -1: # 감소
                flag2 = False

        return flag1 or flag2

    def isVibrate(start, count):
        if count == 5:
            return line[start] == line[start + 2] and line[start + 2] == line[start + 4] and line[start + 1] == line[start + 3]

        if count == 4:
            return line[start] == line[start + 2] and line[start + 1] == line[start + 3]

        if count == 3:
            return line[start] == line[start + 2]

    def isProgression(start, count):
        diff = abs(line[start] - line[start + 1])

        for i in range(count - 1):
            if abs(line[start + i + 1] - line[start + i]) != diff:
                return False

        return True

    def solve(index): # int -> int
        if index >= length:
            return 0

        if index not in memo:
            left = length - index
    
            val = 987654321 # left < 3이면 불가능한 것이므로 임의의 큰 값을 줘서 걸러냄
    
            if left >= 3:
                for count in range(3, max(3 + 1, min(5 + 1, left + 1))):
                    if isSame(index, count):
                        val = min(val, solve(index + count) + 1)
    
                    if isMonotonic(index, count):
                        val = min(val, solve(index + count) + 2)
    
                    if isVibrate(index, count):
                        val = min(val, solve(index + count) + 4)
    
                    if isProgression(index, count):
                        val = min(val, solve(index + count) + 5)
    
                    val = min(val, solve(index + count) + 10)

            memo[index] = val

        return memo[index]

    result = solve(0)

    print(result)