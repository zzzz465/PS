def solution(answers):
    candidates = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0, 0, 0]
    for i in range(len(answers)):
        answer = answers[i]
        for j in range(3):
            if candidates[j][i % len(candidates[j])] == answers[i]:
                scores[j] += 1

    maxValue = max(scores)
    return list(sorted(map(lambda x: x[0] + 1, filter(lambda x: x[1] == maxValue, enumerate(scores)))))

print(solution([1, 3, 2, 4, 2]))