N = int(input())
numbers = [*map(int, input().split())]

# 5로 예시를 들어보자
# 5는 진짜 약수의 개수가 0개이다, 왜냐면 1과 N을 제외한 약수를 구해야 하는데, 그것에 해당하는 것은 없기 때문

result = min(numbers) * max(numbers)

print(result)