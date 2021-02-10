def reverseShuffleMerge(s):
    result = ''
    finding = int(len(s) / 2)
    for i in range(len(s) - 1, 0, -1):
        if s[i-1] > s[i]: # 역순
            result = s[i - finding + 1:i+1]
            break
    
    return ''.join(list(reversed(result)))

result = reverseShuffleMerge('abcdefgabcdefg')

print(result)

result2 = reverseShuffleMerge('aeiouuoiea')

print(result2)
## ????