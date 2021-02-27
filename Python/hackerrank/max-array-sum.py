# 나 이거 제대로 못풀었으니까, 꼼꼼하게 다시 풀어보도록 하자

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    li = [0] * len(arr)
    li[0] = arr[0]
    li[1] = max(arr[0:2])
    for i in range(2, len(li)):
        values = [0] * 3 + [arr[i]]
        values[0] = li[i-1]
        values[1] = li[i-2]
        values[2] = li[i-2] + arr[i]
        
        li[i] = max(values)
        
    return li[len(arr) - 1]

'B'.isupper()
