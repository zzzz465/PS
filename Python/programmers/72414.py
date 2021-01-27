import bisect

def to_second(s: str):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]

    result = int(hour) * 3600
    result += int(minute) * 60
    result += int(second)

    return result

def to_str(time: int):
    hour, time = divmod(time, 3600)
    minute, time = divmod(time, 60)
    second = time

    return '{:0>2}:{:0>2}:{:0>2}'.format(hour, minute, second)


def solution(play_time, adv_time, logs):
    total_time = to_second(play_time)
    time_record = [0 for _ in range(360000)]

    for log in logs:
        start, end = map(to_second, log.split('-'))
        time_record[start] += 1
        time_record[end] -= 1

    for j in range(2):
        for i in range(1, total_time):
            time_record[i] += time_record[i-1]
    
    max_time = 0
    max_i = 0
    at = to_second(adv_time)
    for i in range(at - 1, total_time):
        if i >= at:
            if max_time < time_record[i] - time_record[i-at]:
                max_time = time_record[i] - time_record[i-at]
                max_i = i
            # max_time = max(max_time, time_record[i] - time_record[i - at])
        else:
            if max_time < time_record[i]:
                max_time = time_record[i]
                max_i = i
            # max_time = max(max_time, time_record[i])

    result = to_str(max_i - at + 1)
    return result

if __name__ == '__main__':
    sec1 = to_second('00:00:40')
    str1 = to_str(sec1)

    sec2 = to_second('00:13:03')
    str2 = to_str(sec2)

    play_time_1 = '02:03:55'
    adv_time_1 = '00:14:15'
    logs_1 = [
        '01:20:15-01:45:14',
        '00:40:31-01:00:00',
        '00:25:50-00:48:29',
        '01:30:59-01:53:29',
        '01:37:44-02:02:30'
    ]

    res1 = solution(play_time_1, adv_time_1, logs_1)

    exit(0)