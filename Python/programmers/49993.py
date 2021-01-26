from typing import List
from collections import deque

def solution(skill: str, skill_trees: List[str]):
    count = 0

    available_skills = set([*skill])

    for skill_tree in skill_trees:

        skill_index = 0
        valid = True
        for s in skill_tree:
            if s in available_skills:
                if skill_index != skill.index(s):
                    valid = False
                    break
                else:
                    skill_index += 1

        if valid:
            count += 1

    return count

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))