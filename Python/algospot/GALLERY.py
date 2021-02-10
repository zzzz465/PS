def solve():
    g, h = list(map(int, input().split()))

    adj = [[0] * g] * g
    visited = [False] * g

    for _ in range(h):
        a, b = list(map(int, input().split()))

        adj[a][b] = 1
        adj[b][a] = 1

    totalCCTVCount = 0

    LEAF = 0
    CCTV = 1
    WATCHED = 2

    def checkCCTV(index):
        nonlocal adj, totalCCTVCount, visited

        if visited[index] == True:
            return WATCHED
        else:
            visited[index] = True

        this_state = LEAF
        for other in range(g):
            if adj[index][other] == 1:
                state = checkCCTV(other)
                if state == LEAF:
                    this_state = CCTV
                elif state == CCTV and this_state != CCTV:
                    this_state = WATCHED

        if this_state == CCTV:
            totalCCTVCount += 1

        return this_state

    for i in range(g):
        state = checkCCTV(i)
        if state == LEAF:
            totalCCTVCount += 1

    print(totalCCTVCount)

C = int(input())

for _ in range(C):
    solve()