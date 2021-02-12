
triangle = list()

memo = dict()

def DP(height, index):
    if height == 0:
        return triangle[height][0]

    if index >= height + 1:
        return 0

    if (height, index) in memo:
        return memo[(height, index)]

    max_val = 0
    if index > 0: # 왼쪽
        max_val = DP(height - 1, index - 1)

    if index <= height: # 오른쪽
        max_val = max(max_val, DP(height - 1, index))

    # return max_val + triangle[height][index]
    result = max_val + triangle[height][index]
    memo[(height, index)] = result
    return result

def solution(input):
    global triangle
    triangle = input

    max_val = 0
    for i in range(len(input[len(input) - 1])): # 마지막 index 모음
        max_val = max(max_val, DP(len(input) - 1, i))

    return max_val

if __name__ == '__main__':
    input = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    result = solution(input)

    exit(0)