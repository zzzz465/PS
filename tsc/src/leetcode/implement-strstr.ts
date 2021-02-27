function strStr(haystack: string, needle: string): number {
    if (needle.length === 0)
        return 0
    
    for (let start = 0; start < haystack.length; start++) {
        let i = start, j = 0
        while (i < haystack.length && j < needle.length && haystack[i] === needle[j]) {
            i++; j++;
        }
        
        if (j === needle.length) {
            return start
        }
    }
    
    return -1
};