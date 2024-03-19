class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        subsets: set[str] = set()

        for i in range(len(s) - 1):
            subsets.add(s[i:i+2])

        reversedString = s[::-1]

        for i in range(len(s) - 1):
            reversedSubset = reversedString[i:i+2]
            if reversedSubset in subsets:
                return True

        return False

if __name__ == '__main__':
    assert Solution().isSubstringPresent('leetcode')
    assert Solution().isSubstringPresent('abcba')
    assert not Solution().isSubstringPresent('abcd')

    pass
