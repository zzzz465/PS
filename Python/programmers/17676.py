from datetime import date

def parse(text):
    text, time = text.split(' ')[1:]
    hour = int(text[0:2]) * 3600
    minute = int(text[3:5]) * 60
    second = int(text[6:8])
    millisecond = int(text[9:])
    
    time_second, time_millisecond = (0, 0)
    if '.' in time:
        time_second, time_millisecond = map(int, time.rstrip('s').split('.'))
    else:
        time_second = int(time.rstrip('s'))
    
    end_time_millisecond = (hour + minute + second) * 1000 + millisecond
    duration_millisecond = time_second * 1000 + time_millisecond
    
    return (end_time_millisecond - duration_millisecond + 1, end_time_millisecond)

def check(time, li):
    count = 0
    start = time
    end = time + 1000
    
    for other_start, other_end in li:
        if other_end >= start and other_start < end:
            count += 1
            
    return count

def solution(lines):
    lines = [*map(parse, lines)]
    
    max_count = 0
    for start, end in lines:
        max_count = max(max_count, check(start, lines), check(end, lines))
    
    #3번하고 18번
    # if max_count == 0:
        # max_count = max(max_count, high - low)
    
    answer = max_count
    return answer