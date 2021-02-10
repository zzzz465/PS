def solve():
    N = int(input())

    word_in = [0] * 26
    word_out = [0] * 26
    word_adj = [[0 for _ in range(26)] for _ in range(26)]

    words = [[[] for _ in range(26)] for _ in range(26)] # 시작하는거로

    for _ in range(N):
        word = input()
        startIndex = ord(word[0]) - ord('a')
        endIndex = ord(word[-1]) - ord('a')
        word_in[startIndex] += 1
        word_out[endIndex] += 1

        words[startIndex][endIndex].append(word)
        word_adj[startIndex][endIndex] += 1

    def isEuler():
        plus = 0
        minus = 0
        for i in range(0, 26):
            delta = word_in[i] - word_out[i]
            if abs(delta) > 1:
                return False

            if delta == 1:
                plus += 1
            elif delta == -1:
                minus += 1

        if (plus == 1 and minus == 1) or (plus == 0 and minus == 0):
            return True
        
        return False

    def DFS(here, li): # return what?
        for there in range(26):
            while word_adj[here][there] > 0:
                word_adj[here][there] -= 1
                DFS(there, li)

        li.append(here)

        return li

    result = []

    if isEuler():
        for i in range(0, 26):
            if word_out[i] == word_in[i] + 1:
                result = list(reversed(DFS(i, [])))
                break

        else:
            for i in range(0, 26):
                if word_out[i] == word_in[i] and word_out[i] > 0:
                    result = list(reversed(DFS(i, [])))
                    break

    else:
        return []

    result_string = []
    for i in range(1, len(result)):
        result_string.append(words[result[i-1]][result[i]][-1])
        words[result[i-1]][result[i]].pop()

    return result_string

C = int(input())

for _ in range(C):
    result = solve()
    if len(result) != 0:
        print(' '.join(result))
    else:
        print('IMPOSSIBLE')