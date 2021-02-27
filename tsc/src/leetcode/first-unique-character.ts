function firstUniqChar(s: string): number {
    const a = 'a'.charCodeAt(0)
    const counter = Array(27).fill(0)
    for (const char of s)
        counter[char.charCodeAt(0) - a]++
    
    for (let i = 0; i < s.length; i++) {
        const char = s[i]
        const charCode = char.charCodeAt(0)
        if (counter[charCode - a] == 1)
            return i
    }
    
    return -1
};