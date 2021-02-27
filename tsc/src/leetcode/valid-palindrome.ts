function isPalindrome(s: string): boolean {
    s = s.toLowerCase().split('').filter(d => d.match(/[a-z0-9]/)).join('')
    let lo = 0
    let hi = s.length - 1
    
    while (lo < hi) {
        if (s[lo] !== s[hi]) {
            return false
        }
        
        lo++; hi--;
    }
    
    return true
};