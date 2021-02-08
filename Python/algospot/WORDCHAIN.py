def Index(char):
    return ord(char) - ord('a')

def solve():
    N = int(input())

    word_in = [0] * 26
    word_out = [0] * 26

    words = [[] for _ in range(26)] # 26 * 26 matrix, start -> end
    first_word = ''

    for _ in range(N):
        word = input()
        if _ == 0:
            first_word = word
            continue

        start = word[0]
        startIndex = ord(start) - ord('a')
        end = word[-1]
        endIndex = ord(end) - ord('a')

        word_in[startIndex] += 1
        word_out[endIndex] += 1

        words[startIndex].append(word)

    def checkEuler(): # euler circuit or trail
        plus = 0
        minus = 0
        for i in range(0, 26):
            delta = word_out[i] - word_in[i]
            if abs(delta) > 1:
                return False
            else:
                if delta == 1:
                    plus += 1
                elif delta == -1:
                    minus += 1
        
        return (plus == 1 and minus == 1) or (plus == 0 and minus == 0)


    def EulerPath(thisWord, result):
        # nonlocal word_in #, word_out
        nonlocal words

        start = Index(thisWord[0])
        end = Index(thisWord[-1])

        while len(words[end]) > 0:
            otherWord = words[end].pop()
            # word_in[Index(otherWord[0])] -= 1
            EulerPath(otherWord, result)

        result.append(thisWord)

    if checkEuler():
        result = []
        for i in range(0, 26):
            if word_in[i] + 1 == word_out[i]:
                first_word = words[i].pop()
                result.append(first_word)
                EulerPath(first_word, result)
                break

        if len(result) == 0:
            for i in range(0, 26):
                if word_in[i] == word_out[i]:
                    first_word = words[i].pop()
                    result.append(first_word)
                    EulerPath(first_word, result)

        if len(result) != len(words) + 1:
            return False

        result.reverse()
        return result
            
    else:
        return False


C = int(input())

for _ in range(C):
    result = solve()

    if result != False:
        print(' '.join(result))
    else:
        print('IMPOSSIBLE')