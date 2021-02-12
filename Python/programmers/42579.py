from collections import Counter
from typing import List
from functools import cmp_to_key

def solution(genres: List[str], plays: List[int]):
    song_collections = dict() # 장르 - List[[index, song_count]]
    song_count = Counter()

    for index in range(len(genres)):
        genre, play = genres[index], plays[index]

        if genre not in song_collections:
            song_collections[genre] = list()

        song_collections[genre].append([index, plays[index]])

        song_count[genre] += play

    result = []

    def compare(x, y):
        if x[1] != y[1]:
            return y[1] - x[1]

        else:
            return x[0] - y[0]

    for name, count in song_count.most_common(): # 가장 많이 재생된 곡 재생
        songs = song_collections[name] #List[[index, song_count]]
        songs.sort(key=cmp_to_key(compare)) # 많이 재생된 곡 수행

        for index, _ in songs[0:2]:
            result.append(index)

    return result

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))