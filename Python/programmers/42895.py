from collections import deque, defaultdict
from itertools import combinations, permutations

def solution(N, number):
    answer = 987654321
    
    memo = defaultdict(set)
    val = 0
    for i in range(1, 8 + 1):
        val *= 10
        val += N
        memo[i].add(val)
        
    for i in range(2, 8+1):
        start = 1
        end = i - start
        
        while start <= end:
            # do-something
            start_values = [*memo[start]]
            end_values = [*memo[end]]
            for val1 in start_values:
                for val2 in end_values:
                    # 덧셈
                    memo[i].add(val1 + val2)
                    # 뺄셈
                    memo[i].add(val1 - val2)
                    memo[i].add(val2 - val1)
                    # 곱셈
                    memo[i].add(val1 * val2)
                    #나눗셈
                    if (val2 != 0):
                        memo[i].add(int(val1 / val2))
                    if val1 != 0:
                        memo[i].add(int(val2 / val1))

            start += 1
            end -= 1
        
    for i in range(1, 8+1):
        if number in memo[i]:
            answer = i
            break
        
    if answer > 8:
        return -1
    else:
        return answer

if __name__ == '__main__':
    solution(5, 12)
    pass