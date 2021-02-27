class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        textMinLength = min(map(len, strs))
        
        commonPrefixes = [] # string[]
        for i in range(textMinLength):
            c = strs[0][i]
            match = True
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    match = False
                    break
                    
            if match:
                commonPrefixes.append(c)
            else:
                break
                
        return ''.join(commonPrefixes)
        