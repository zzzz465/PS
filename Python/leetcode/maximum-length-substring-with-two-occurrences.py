from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # since there's no limit about memory (usually ~512MB?)
        # and also len(s) is limited to 100
        # just use two-pointer logic for creating substring
        # and calculate that the substring matches the given condition

        # we store largest length of substring in this variable
        largest = -1

        # substr: i <= x < j
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                # create substring using two pointer
                substr = s[i:j]

                # checks each character appears at most two times
                counts = defaultdict(int)
                for c in substr:
                    counts[c] += 1

                if all(map(lambda x: x <= 2, counts.values())):
                    largest = max(len(substr), largest)

        return largest


if __name__ == "__main__":
    assert Solution().maximumLengthSubstring("bcbbbcba") == 4
