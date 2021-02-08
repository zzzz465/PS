C = int(input())

for _ in range(C):
    N = int(input())

    char_map = [set()] * 26
    visited = [False] * 26

    texts = [input()]

    for i in range(N - 1):
        text = input()
        before = texts[-1]

        if before > text:
            for b, t in zip(before, text):
                if b > t:
                    char_map[ord(b) - ord('a')].add(t)
                    break

        texts.append(text)

    result = []
    def DFS(index):
        global char_map, visited
        if visited[index]:
            return
        else:
            visited[index] = True

        result.append(index)

        for other in map(lambda x: ord(x) - ord('a'), char_map[index]):
            DFS(other)

    for i in range(26):
        DFS(i)

    result = list(map(lambda x: chr(ord('a') + x), reversed(result)))

    print(result)