import math

def solution(brown, yellow):
    answer = []

    area = brown + yellow
    
    for height in range(3, int(math.sqrt(area)) + 1):
        width = area / height
        if width % 1 == 0:
            if (width * 2 + height * 2) - 4 == brown:
                answer.append(int(width))
                answer.append(height)
                break

    return [*reversed(sorted(answer))]

for brown, yellow in [[10, 2], [8, 1], [24, 24]]:
    print(solution(brown, yellow))