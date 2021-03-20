N = int(input())
times = [input() for _ in range(N)]

timeArray = [0] * (24 * 60) # 분 단위로 계산, 00:00 ~ 23:59

# [[hour, minute], [hour, minute]] (start, end)
def timeStringToTimeArray(data: str):
    start, end = [*map(lambda text: text.strip().split(':'), data.split('~'))]
    startTime = int(start[0]) * 60 + int(start[1])
    endTime = int(end[0]) * 60 + int(end[1])

    return [startTime, endTime]

def minuteToTimeString(time: int):
    hour = time // 60
    minute = time % 60
    return f'{hour:02d}:{minute:02d}'

arr = []

for time in times:
    start, end = timeStringToTimeArray(time)
    arr.append((start, 1))
    arr.append((end, -1))

count = 0
startTime = -1
endTime = -1
for op in sorted(arr):
    time, opcode = op
    if opcode == 1:
        count += 1
        if count == N:
            startTime = time
    else:
        if count == N:
            endTime = time
        count -= 1


if startTime == -1:
    print(-1)
else:
    startTimeStr = minuteToTimeString(startTime)
    endTimeStr = minuteToTimeString(endTime)
    print(f'{startTimeStr} ~ {endTimeStr}')
