import re

def solution(new_id: str):
    new_id = new_id.lower() # 1
    li = []
    for char in new_id:
        if str.islower(char) or str.isdigit(char) or char == '-' or char == '_' or char == '.':
            li.append(char)

    new_id = ''.join(li)
    new_id = re.sub('\.{2,}', '.', new_id)
    new_id = new_id.strip('.')

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[0:15]
    
    new_id = new_id.strip('.')
    
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id

if __name__ == '__main__':
    text1 = '...!@BaT#*..y.abcdefghijklm'
    result1 = solution(text1)

    text2 = 'z-+.^.'
    result2 = solution(text2)

    exit(0)