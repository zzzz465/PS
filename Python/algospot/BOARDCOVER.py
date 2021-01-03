import os

shapes = [ # 시작지점을 기준으로 가능한 모양, (x, y)
    [(0, 0), (1, 0), (1, 1)], # ㄱ
    [(0, 0), (0, 1), (-1, 1)], # ㄴ 좌우반전
    [(0, 0), (0, 1), (1, 1)], # ㄴ
    [(0, 0), (0, 1), (1, 0)] # ㄱ 반시계
]

# 좌측 위에서 시작하는거니까, 가능한 모양이 정해져있음
# L자 블록만 가능

# (x, y) 만 사용하자

N = int(input())
for _ in range(N):
    height, width = list(map(int, input().split()))

    elementSize = width * height

    board = list()
    for _ in range(height):
        input_data = filter(lambda x: x == '#' or x == '.', input())
        board.append(list(map(lambda x: x == '#', input_data))) # 검은칸은 True, 하얀 칸은 F

    # 왼쪽 위부터 시작해보자
    def placeable(pos, shape):
        flag = True
        for x, y in shape: # 한번이라도 이미 점유중인 공간은 사용불가능
            posX, posY = pos[0] + x, pos[1] + y
            if 0 <= posY and posY < height and 0 <= posX and posX < width: # insdie the box
                if board[posY][posX]:
                    flag = False
            else:
                return False
        
        return flag

    def place(pos, shape):
        posX, posY = pos
        for x, y in shape:
            board[posY + y][posX + x] = True

    def unplace(pos, shape):
        posX, posY = pos
        for x, y in shape:
            board[posY + y][posX + x] = False

    def find_min(): # 성공시 (x, y), 실패 시 (-1, -1)
        for y in range(height):
            for x in range(width):
                if 0 <= y and y < height and 0 <= x and x < width:
                    if not board[y][x]:
                        return (x, y)

        return (-1, -1)

    count = 0

    def solve():
        global count
        x, y = find_min()
        if x == -1:
            count += 1

        for shape in shapes:
            if placeable((x, y), shape):
                place((x, y), shape)
                solve()
                unplace((x, y), shape)

    solve()

    print(count)