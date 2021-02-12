
memo = dict()
jumpCount = 0
position = 0

def moveTo(n: int):
    global jumpCount, position

    if position < int(n / 2):
        if position == 0:
            position += 1
            jumpCount += 1
            moveTo(n)
        else:
            moveTo(int(n / 2))
            position *= 2
            if n - position == 1:
                jumpCount += 1
                position += 1
    
    elif position == int(n / 2):
        position *= 2

    else:
        jumpCount += n - position
        position = n

def solution(n: int):
    global jumpCount, position
    position = 0
    jumpCount = 0

    moveTo(n)

    return jumpCount

for n in [5, 6, 5000]:
    print(solution(n))