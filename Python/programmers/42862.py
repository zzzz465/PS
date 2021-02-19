def solution(n, lost, reserve):
    reserve = set(reserve)
    lost = set(lost)
    
    for id in sorted(list(lost)):
        if (id - 1) in reserve:
            lost.remove(id)
            reserve.remove(id - 1)
            
        elif (id + 1) in reserve:
            lost.remove(id)
            reserve.remove(id + 1)
            
    count = n - len(lost)

    return count

solution(5, [2, 4], [3])