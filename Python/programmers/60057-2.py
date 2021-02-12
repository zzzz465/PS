from typing import Counter


def solution(s: str):
    min_length = 987654321
    for length in range(1, int(len(s) / 2) + 1):
        counter = Counter()
        index = 0
        while index + length <= len(s):
            chunk = s[index:index + length]
            counter[chunk] += 1
            index += length

        result = s
        index = 0
        while index + length < len(result):
            chunk = result[index:index+length]
            if chunk in counter:
                count = 0

                start = index
                while True:
                    if result[index:index+length] == chunk:
                        count += 1
                        index += length
                    else:
                        break

                if count > 1:
                    result = result[0:start] + str(count) + chunk + result[start + length * count:]
                    index = start + 1 + length
                else:
                    index = start + length

        # for key, count in counter.most_common():
            # search_index = 0
            # while True:
                # start = result.find(key, search_index)
                # if start == -1:
                    # break
# 
                # count = 0
                # index = start
                # while True:
                    # if result[index:index+length] == key:
                        # count += 1
                        # index += length
                    # else:
                        # break
# 
                # if count > 1: # 압축
                    # result = result[0:start] + str(count) + key + result[start + length * count:]
                    # search_index = start + 1 + length
                # else:
                    # search_index = index + length

        min_length = min(min_length, len(result))

    return min_length

if __name__ == '__main__':
    res = solution('abcabcabcabcdededededede')

    exit(0)