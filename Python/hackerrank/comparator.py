from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass
        
    def comparator(a, b):
        if a.score != b.score:
            return -(a.score - b.score)
        else:
            if a.name < b.name:
                return -1
            else: # no same name
                return 1

n = int(input())