N, M = map(int, input().split()) # N은 가로, M은 세로

board = [[input()] for _ in range(N)]

for i in range(0, N - 8 + 1):
    for j in range(0, M - 8 + 1):
        
        # 시작이 W일때
        # 시작이 B일때
