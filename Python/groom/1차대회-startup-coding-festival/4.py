from functools import cmp_to_key

A, B, C, D, E = map(float, input().split())
genrePreferenceMap = { 'A': A, 'B': B, 'C': C , 'D': D, 'E': E }
N, M = map(int, input().split())

records = [[*input()] for _ in range(N)]
genres = [[*input()] for _ in range(N)]

# entries = [*zip(records, genres, [[(i, j) for j in range(M)] for i in range(N)])] # [[record, genre, pos]] (pos = (y, x))

entries = [] # record, genre, pos

for i in range(N):
    for j in range(M):
        entries.append((records[i][j], genres[i][j], (i, j)))

def sortFunc(a, b):
    a_record = a[0]
    b_record = b[0]

    if a_record != b_record: # compare by record type
        if a_record == 'Y':
            return -1
        elif a_record == 'O':
            if b_record == 'W':
                return -1
            else:
                return 1
        else:
            return 1

    a_genre = a[1]
    b_genre = b[1]
    
    if a_genre != b_genre: # compare by genre order
        return - (genrePreferenceMap[a_genre] - genrePreferenceMap[b_genre])

    return a[2] < b[2] # compare by position


entries = [*filter(lambda x: x[0] != 'W', entries)]
entries.sort(key=cmp_to_key(sortFunc))

for entry in entries:
    genre = entry[1]
    preference = genrePreferenceMap[genre]
    y, x = entry[2]

    print(f'{genre} {preference} {y} {x}')