found = False
def solve(modify, match):
    global found
    if len(match) == 0:
        if len(modify) > 0:
            if modify.islower():
                found = True
                
        else:
            found = True
                
        return
    
    if len(modify) == 0:
        return
    
    i = 0
    j = 0
    
    for i in range(len(match)):
        match_letter = match[i]
        
        while j < len(modify):
            char = modify[j]
            if char.isupper():
                if char == match_letter:
                    solve(modify[j+1:], match[i+1:])
                else:
                    return
            else:
                if char.upper() == match_letter:
                    solve(modify[j+1:], match[i+1:])

            j += 1
        
        i += 1

C = int(input())

for _ in range(C):
    modify = input()
    match = input()
    
    found = False
    solve(modify, match)
    print('YES' if found else 'NO')