from typing import Counter


def solution(s: str):
    min_length = 987654321

    for length in range(1, int(len(s) / 2) + 1):
        result = s
        index = 0
        while index + length <= len(result):
            chunk = result[index:index + length]
            
            count = 0
            inner_index = index
            while True:
                other = result[inner_index:inner_index + length]
                if other == chunk:
                    count += 1
                    inner_index += length
                else:
                    break

            if count > 1:
                result = result[0:index] + str(count) + chunk + result[index + length * count:]
                index = index + 1 + length
            else:
                index = index + length
            
        min_length = min(min_length, len(result))

    if min_length == 987654321:
        return len(s)

if __name__ == '__main__':
    res = solution('a')

    exit(0)