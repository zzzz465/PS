
# x는 4분할을 하겠다 라고 표시하는 헤더
# w는 한 공간이 전부 하얀색임을 나타냄
# b는 한 공간이 전부 검은색임을 나타냄

N = int(input())

for _ in range(N):
    compressed = input()

    '''
    상하로 뒤집는다는 의미는
    1 2  -> 3 4
    3 4     1 2
    이며, 1 2 3 4 자체도 상하로 뒤집힌다는 것이다.
    이 때, w, b는 뒤집어도 바뀌는 것이 없으므로 base case 이다.
    '''

    def solve(text): # (text: string) -> (string, string) 뒤집힌 결과, 그리고 남은 문자열들
        if text == 'b' or text == 'w': # 단 한개 일 경우
            return (text, '')

        if text[0] == 'x':
            first, left = solve(text[1:])
            second, left = solve(left)
            third, left = solve(left)
            forth, left = solve(left)
            result = 'x' + third + forth + first + second
            return (result, left)
        
        else: # 1글자 (b, w) 도 아닌데 x로 시작하지도 않음 -> 더이상 쪼갤 수 없는 4분할 상태
            return (text[0], text[1:])

    result, _ = solve(compressed)

    print(result)