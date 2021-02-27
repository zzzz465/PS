function isAnagram(s: string, t: string): boolean {
    const s_counter = Array(26).fill(0)
    const t_counter = Array(26).fill(0)
    
    const a_charCode = 'a'.charCodeAt(0)
    
    for (const char of s) {
        const index = char.charCodeAt(0) - a_charCode
        s_counter[index] += 1
    }
    
    for (const char of t) {
        const index = char.charCodeAt(0) - a_charCode
        t_counter[index] += 1
    }
    
    for (let i = 0; i < 26; i++) {
        if (s_counter[i] != t_counter[i])
            return false
    }
    
    return true
};