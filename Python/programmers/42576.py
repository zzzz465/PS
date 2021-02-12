from typing import List


def solution(participant: List[int], completion: List[int]):
    participant.sort(); completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]