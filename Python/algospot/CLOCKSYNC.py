import sys

N = int(input())

# 0 -> 0, 1 -> 3, 2 -> 6, 3 -> 9

d = {
    0: [0, 1, 2],
    1: [3, 7, 9, 11],
    2: [4, 10, 14, 15],
    3: [0, 4, 5, 6, 7],
    4: [6, 7, 8, 10, 12],
    5: [0, 2, 14, 15],
    6: [3, 14, 15],
    7: [4, 5, 7, 14, 15],
    8: [1, 2, 3, 4, 5],
    9: [3, 4, 5, 9, 13]
}

def convert(num):
    if num == 12:
        return 0
    elif num == 3:
        return 1
    elif num == 6:
        return 2
    elif num == 9:
        return 3

for _ in range(N):
    numbers = list(map(lambda num: convert(int(num)), sys.stdin.readline().split())) # int[16]

    minPressCount = 987654321

    def set(index, number, flag): # index 번의 버튼을 number 번 누름, flag = true 일 경우 누르기, flag = false 일경우 누른거 취소
        for i in d[index]:
            if flag:
                numbers[i] = (numbers[i] + number) % 4
            else:
                numbers[i] = (numbers[i] - number) % 4

    def solve(pressCount, index): # 버튼 인덱스
        global minPressCount
        if pressCount > minPressCount: # 답이 안나왔는데 벌써 값을 넘겼을 경우 다음 버튼들을 전부 0 눌러도 최솟값 갱신 불가능
            return

        if index == 10:
            if all(map(lambda x: x == 0, numbers)):
                if pressCount < minPressCount:
                    minPressCount = pressCount

        else:
            for i in range(4): # index 버튼을 i번 누름
                set(index, i, True)
                solve(pressCount + i, index + 1)
                set(index, i, False)

    solve(0, 0)

    if minPressCount == 987654321:
        minPressCount = -1

    print(minPressCount)