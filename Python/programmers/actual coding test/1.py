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
                    
                    if snowball == otherSnowball: # 같이 부셔짐 -> 종료
                        snowballs[index] = None
                        break
                
                else: # 내가 부셔짐 -> 종료
                    snowballs[index] = None
                    break
                    
        otherIndex += direction

def solution(snowballs):
    
    while True:
        allSame = True
        for i in range(len(snowballs) - 1):
            if not sameDirection(snowballs[i], snowballs[i+1]):
                allSame = False
                break
                
        if allSame:
            break

        else:
            for i in range(1, len(snowballs) - 1):
                destroyAllSnowballsAgainst(snowballs, i)
            
            snowballs = list(filter(lambda x: x != None, snowballs))
    
    return snowballs

solution([1, 5, -5, 5, ])