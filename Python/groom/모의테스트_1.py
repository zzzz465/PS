from sys import maxsize

_, N = map(int, input().split())
nums = [*map(int, input().split())]
minValue = min(nums)

totalAdjustCount = 0

while True:
    for minIndex in range(len(nums)):
        if nums[minIndex] == minValue: # 항상 연속적인 최솟값으로 이루어진 배열의 양 끝단을 선택해야 함
            if minIndex > 0 and nums[minIndex - 1] == minValue and minIndex < len(nums) - 1 and nums[minIndex + 1] == minValue:
                continue

            selectedIndex = -1
            maxCount = 0
            for i in range(N): # index of minimum value in normalization
                if 0 <= minIndex - i and minIndex - i + N <= len(nums):
                    count = len([*filter(lambda x: x > minValue, nums[minIndex - i:minIndex - i + N])])
                    if count > maxCount:
                        selectedIndex = i
                        maxCount = count
        
            if selectedIndex != -1:
                for i in range(minIndex - selectedIndex, minIndex - selectedIndex + N):
                    nums[i] = minValue
                
                totalAdjustCount += 1
                print(nums)
                break

    else:
        break
    
print(totalAdjustCount)