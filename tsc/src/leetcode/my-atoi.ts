function myAtoi(s: string): number {
    let index = 0
    
    // skip whitespaces
    while (index < s.length && s[index] === ' ')
        index += 1;
    
    // check operator
    let operator: string | undefined = undefined
    if (s[index] == '+' || s[index] == '-')
        operator = s[index++]
    
    const _0 = '0'.charCodeAt(0)
    const _9 = '9'.charCodeAt(0)
    
    let digits: string[] = []
    
    // ignore number start with zero
    while (index < s.length && s[index].charCodeAt(0) === _0)
        index++
    
    // collect digits
    while (index < s.length && _0 <= s[index].charCodeAt(0) && s[index].charCodeAt(0) <= _9) {
        digits.push(s[index++])
    }
    
    let lower_bound = 1 << 31 // 32bit lowest number
    
    let upper_bound = 0 // 32bit highest number
    for (let i = 0; i < 31; i++) {
        upper_bound = upper_bound << 1
        upper_bound |= 1
    }
    
    if (digits.length > 0) {
        const numberStr = digits.join('')
        if (operator === '-') {
            const lower_bound_str = String(Math.abs(lower_bound))
            if (numberStr.length > lower_bound_str.length ||
                (numberStr.length == lower_bound_str.length && numberStr > lower_bound_str)) {
                // 값을 초과했을 경우
                return lower_bound
            } else {
                return -numberStr
            }
        } else {
            const upper_bound_str = String(upper_bound)
            if (numberStr.length > upper_bound_str.length ||
               (numberStr.length == upper_bound_str.length && numberStr > upper_bound_str)) {
                return upper_bound
            } else {
                return +numberStr
            }
        }
    } else {
        // no digits to read
        return 0
    }
};