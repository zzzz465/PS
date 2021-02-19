from functools import cmp_to_key

N = int(input())

words = set()
for i in range(N):
    words.add(input())

def compare(x, y):
    if len(x) != len(y):
        return len(x) - len(y)
    else:
        for a, b in zip(x, y):
            if a < b:
                return -1
            if a > b:
                return 1

        return 0

for word in sorted(words, key=cmp_to_key(compare)):
    print(word)