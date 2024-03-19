from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        '''
        1. 각 char 별 freq 계산
        2. ???
        '''

        wordCount: dict[str, int] = defaultdict(int)
        deletedCount = 0

        for c in word:
            wordCount[c] += 1

        while True:
            minCount = 99999999999999
            minCountChar = ''
            maxCount = -1
            maxCountChar = ''
            squareSum = 0
            charCount = 0

            for char, count in wordCount.items():
                if count == 0:
                    continue

                if count < minCount:
                    minCount = count
                    minCountChar = char
                
                if count > maxCount:
                    maxCount = count
                    maxCountChar = char

                squareSum += count^2
                charCount += 1

            # all string is removed (should not occur)
            if minCountChar == '' or maxCountChar == '':
                return -1
            elif abs(maxCount - minCount) <= k:
                break

            ground = squareSum / charCount

            # weight check
            # max 쪽이 더 차이가 크므로, max 쪽을 더 깎아서 diff 를 만들자
            if abs(ground - minCount) < abs(ground - maxCount):
                wordCount[maxCountChar] -= 1
            elif abs(ground - minCount) < abs(ground - maxCount):
                wordCount[minCountChar] -= 1
            else:
                # when the value is same (멸망전)
                if abs(k - minCount) > abs(k - maxCount):
                    wordCount[minCountChar] -= wordCount[minCountChar]
                else:
                    wordCount[maxCountChar] -= wordCount[maxCountChar]

            deletedCount += 1


        return deletedCount

if __name__ == '__main__':
    assert Solution().minimumDeletions('aabcaba', 0) == 3
    # assert Solution().minimumDeletions('dabdcbdcdcd', 2) == 2
    # assert Solution().minimumDeletions('aaabaaa', 2) == 1
    # assert Solution().minimumDeletions('ahahnhahhah', 1) == 2
