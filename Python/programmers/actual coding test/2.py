# 1. "예티"는 원하는 크기의 눈덩이를 만든다
# 2. 왼쪽 또는 오른쪽으로만 던진다
# 3. 눈덩이는 같은 속력으로 이동
# 4. 눈덩이들끼리 충돌하면 작은 눈덩이는 바로 떨어지고, 큰 눈덩이는 그대로 직진
# 5. 눈덩이 개수보다 실제로 피해야 하는 눈덩이는 적을 수 있다.
# 6. (같은 것은 상쇄되어 사라짐)

# 신경써야 하는 눈덩이들을 반환하라
# 예티 수 1~5000개
# 눈덩이 크기 1~1000
# 양수 -> 오른쪽으로 이동, 음수 -> 왼쪽으로 이동

# linkedList 쓰면 될 것 같은데...
# 굳이 지워야하나?
# 중앙을 기준으로 지워지기만 하나?

def canDestroy(curr, other):
    return abs(curr) >= abs(other)

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def sameDirection(curr, other):
    return sign(curr) == sign(other)


def destroyAllSnowballsAgainst(snowballs, index):
    snowball = snowballs[index]
    if snowball == None:
        return
    
    direction = 1 if snowball > 0 else -1
    otherIndex = index + direction
    
    while 0 <= otherIndex < len(snowballs):
        otherSnowball = snowballs[otherIndex]
        if otherSnowball != None:
            if sameDirection(snowball, otherSnowball): # 같은방향 -> 종료
                break

            else:
                if canDestroy(snowball, otherSnowball):
                    snowballs[otherIndex] = None
                    
                    if abs(snowball) == abs(otherSnowball): # 같이 부셔짐 -> 종료
                        snowballs[index] = None
                        break
                
                else: # 내가 부셔짐 -> 종료
                    snowballs[index] = None
                    break
                    
        otherIndex += direction

def solution(snowballs):
    
    while True:
        ordered = True # 종료 조건
        for i in range(len(snowballs) - 1):
            if sign(snowballs[i]) > sign(snowballs[i+1]):
                ordered = False
                break

        if ordered:
            break

        else:
            for i in range(0, len(snowballs) - 1):
                destroyAllSnowballsAgainst(snowballs, i)
            
            snowballs = list(filter(lambda x: x != None, snowballs))
    
    return snowballs

# solution([1,5,-5,5,-5,5,-5,-2])
solution([-5, 5])