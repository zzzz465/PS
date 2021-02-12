from collections import Counter

def solution(a):
    max_len = 0

    counter = Counter(a)
    for key, amount in counter.most_common():
        index = len(a) - 1
        
        count = 0
        while index >= 0:
            if a[index] == key:
                while index > 0:
                    index -= 1
                    if a[index] != key:
                        count += 1
                        break

            else:
                while index > 0:
                    index -= 1
                    if a[index] == key:
                        count += 1
                        break

            index -= 1

        if max_len < count:
            max_len = count
        else:
            break

    answer = max_len * 2

    return answer

if __name__ == '__main__':
    zero = solution([0])
    four = solution([5, 2, 3, 3, 5, 3])
    eight = solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0])

    exit(0)