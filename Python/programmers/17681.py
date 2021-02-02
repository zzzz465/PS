def solution(n, arr1, arr2):
    result = [[' '] * n for _ in range(n)]
    
    values = zip(arr1, arr2)
    for i, [val1, val2] in zip([*range(n)], values):
        for j in range(n-1, -1, -1):
            flag = val1 & 1 | val2 & 1
            val1 = val1 >> 1
            val2 = val2 >> 1
            
            if flag != 0:
                result[i][j] = '#'
                    
    return result

if __name__ == '__main__':
    res = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])