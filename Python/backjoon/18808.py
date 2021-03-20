N, M, K = map(int, input().split())

result = [[0] * M for _ in range(N)]

def rotate(matrix) -> None: # 시계방향 90도
    N = len(matrix)
    M = len(matrix[0])
    newMatrix = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            newMatrix[j][N - i - 1] = matrix[i][j]
    
    return newMatrix

for i in range(K):
    R, C = map(int, input().split())
    sticker = [None] * R
    # read sticker
    for j in range(R):
        sticker[j] = [*map(int, input().split())] # width: C

    applied = False

    for rotateCount in range(4): # 회전
        if applied:
            break

        if rotateCount != 0:
            # rotate
            sticker = rotate(sticker)
            R, C = C, R

        for y in range(N - R + 1):
            for x in range(M - C + 1):
                valid = True
                for b in range(R):
                    for a in range(C):
                        if sticker[b][a] == 1 and result[y + b][x + a] == 1:
                            valid = False
                            break
    
                    if not valid:
                        break
    
                if valid:
                    for b in range(R):
                        for a in range(C):
                            if sticker[b][a] == 1:
                                result[y + b][x + a] = 1
    
                    applied = True
                    break
    
            if applied:
                break
    
    # if applied:
        # print('---')
        # for i in range(N):
            # for j in range(M):
                # print(result[i][j], end=' ')
            # print()
        # print('---')

# print('==DEBUG==')
count = 0
for i in range(N):
    for j in range(M):
        if result[i][j] == 1:
            count += 1

        # debug
        # print(result[i][j], end=' ')

    # print()

print(count)