N, M = map(int, input().split())

r, c, d = map(int, input().split())

room = [None] * N
for i in range(N):
    room[i] = list(map(int, input().split()))

direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # y, x

clearCount = 0
def clean():
    global room, r, c, d, clearCount
    return room[r][c] == 1

def clear():
    global room, r, c, d, clearCount
    room[r][c] = 1
    clearCount += 1

def leftState(): # 0 -> dirty, 1 -> clean, 2 -> unreachable
    global direction, r, c, d
    newY = r + direction[(d - 1 + 4) % 4][0]
    newX = c + direction[(d - 1 + 4) % 4][1]

    if 0 <= newY < N and 0 <= newX < M:
        return room[newY][newX]
    else:
        return 2

def allUnreachable():
    global direction, r, c, d

    for offset in direction:
        newY, newX = (r + offset[1], c + offset[0])

        if 0 <= newY < N and 0 <= newX < M and room[newY][newX] == 0:
            return False

    return True

def backIsWall():
    global direction, r, c, d
    offset = direction[(d + 2 + 4) % 4]
    newY = r + offset[0]
    newX = c + offset[1]

    if newY < 0 or newY >= N or newX < 0 or newX >= M:
        return True

    else:
        return False

def advance(distance: int):
    global d, r, c
    r += direction[d][0] * distance
    c += direction[d][1] * distance

def rotate():
    global d # 0 북, 1 동, 2 남, 3 서
    d = (d + 1) % 4

while True:
    if not clean():
        clear()

    else:
        if not leftState():
            rotate() # left
            advance(1)

        elif allUnreachable():
            if backIsWall():
                break # EXIT POINT

            else:
                advance(-1) # 한 칸 후진
        
        else:
            raise Exception()

print(clearCount)
