N, M = map(int, input())
r, c, d = map(int, input())
# d -> 0 = 북쪽, 1 = 동쪽, 2 = 남쪽, 3 = 서쪽

room = [None] * N
for i in range(N):
    room[i] = list(map(int, input().split()))

def currPosCleaned():
    pass

def clearCurrPos():
    pass

def areaToClearExists():
    pass

def advance():
    pass

def rotate():
    pass

def areaAllClearedOrUnreachable():
    pass

def backIsWall():
    pass

while True:
    if not currPosCleaned():
        clearCurrPos()

    else:
        if areaToClearExists():
            rotate(direction)
            advance(direction)

        elif areaAllClearedOrUnreachable():
            if backIsWall():
                break # EXIT

            else:
                advance(direction)

        else:
            
