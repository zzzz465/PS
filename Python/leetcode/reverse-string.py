class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i, j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
        
        for i in range(len(s) // 2):
            hi = (len(s) - 1) - i
            swap(i, hi)