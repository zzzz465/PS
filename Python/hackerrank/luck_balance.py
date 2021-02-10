

def luckBalance(k, contents):
    importants = []
    not_importants = []

    for content in contents:
        if content[1] == 1:
            importants.append(content)
        else:
            not_importants.append(content)

    importants.sort(key=lambda x: x[0])
    
    luckSum = 0
    while k > 0 and len(importants) > 0:
        content = importants.pop()
        luckSum += content[0]
        k -= 1

    for content in importants:
        luckSum -= content[0]

    for content in not_importants:
        luckSum += content[0]

    return luckSum

luckBalance(3, [
    [5, 1],
    [2, 1],
    [1, 1],
    [8, 1],
    [10, 0],
    [5, 0]
])