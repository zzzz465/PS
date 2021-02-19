import heapq
from collections import deque

def solution(jobs):
    jobs_count = len(jobs)
    jobs = deque(sorted(jobs))
    work_queue = []
    time = 0

    work_time = 0
    curr_work = None # None or li

    total_waiting = 0

    while True:
        while len(jobs) > 0:
            if jobs[0][0] <= time:
                heapq.heappush(work_queue, jobs[0][::-1]) # 남은 시간이 적은 것부터 정렬
                jobs.popleft()
            else:
                break

        if curr_work != None:
            if work_time > 0:
                work_time -= 1

            if work_time == 0:
                total_waiting += time - curr_work[1] # 종료 시간 - 요청 시간
                curr_work = None

        if curr_work == None:
            if len(work_queue) > 0:
                curr_work = heapq.heappop(work_queue)
                work_time = curr_work[0]
            else:
                if len(jobs) == 0:
                    break

        time += 1

    answer = total_waiting // jobs_count

    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))