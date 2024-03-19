class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        # count = 0
        occurances: list[int] = []
        # 중복조합 n H 2 인데, 이는 n+r-1 C n-1 기준으로 n+1 C n-1 -> (n+1)!/2!(n-1)! -> (n+1)(n) / 2

        for i in range(len(s)):
            if s[i] == c:
                occurances.append(i)

        n = len(occurances)

        result = int((n+1) * n / 2)
        return result

if __name__ == '__main__':
    assert Solution().countSubstrings('abada', 'a') == 6
    assert Solution().countSubstrings('zzz', 'z') == 6

    pass
