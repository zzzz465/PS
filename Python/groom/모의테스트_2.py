T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # 개당 N 은 5개이상, N+M 은 12 이상

    count = 0
    
    count += min(N // 5, M // 7) # 스페셜 쿠폰을 최소한으로 썼을 때, 얻을 수 있는 개수
    N -= count * 5 # 위에서 쓴 만큼 빼기
    M -= count * 7

    if N >= 5 and N + M >= 12:
        M -= (12 - N)
        count += 1

    print(count)