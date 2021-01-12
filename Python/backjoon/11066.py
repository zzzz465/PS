from typing import List

# very very very very NAIVE solving

C = int(input())
INF = 987654321

for _ in range(C):
    N = int(input())

    numbers = list(map(int, input().split()))
    result = sum(numbers)

    def solve(li: List[int], count: int):
        global result
        if count >= result:
            return

        if len(li) == 1:
            result = min(result, count)
            return

        # i, j 번째 것들을 선택

        for i in range(len(li)):
            for j in range(i + 1, len(li)):
                val1, val2 = li[i], li[j]

                new_list = list(li)
                del new_list[j]
                del new_list[i]
                new_list.append(val1 + val2)

                solve(new_list, count + val1 + val2)

    solve(numbers, 0)

    print(result)