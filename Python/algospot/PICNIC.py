# star function is not working on python version 3.4.3
import sys

N = int(input())
friends = set()
for _ in range(N):
    friends.clear()
    n, m = map(int, input().split())

    data = list(map(int, sys.stdin.readline().split()))
    for i in range(0, len(data), 2):
        a, b = data[i:i+2]
        if a <= b:
            friends.add((a, b))
        else:
            friends.add((b, a))

    count = 0

    def find(available_friends):
        # 종료 조건: 한명도 남지 않을 경우 or 둘만 남았는데 서로 친구가 아닐 경우
        # 한명도 안남을 경우 -> OK, 서로 친구가 아님 -> 해당X
        global count
        lowest = min(available_friends)
        available_friends.remove(lowest)
        for i in range(lowest + 1, n):
            if i in available_friends and (lowest, i) in friends: # 만약 친구일 경우
                available_friends.remove(i)
                if len(available_friends) > 0:
                    find(available_friends)
                else:
                    count += 1
                available_friends.add(i)

        available_friends.add(lowest)

    find(set(range(n)))

    print(count)