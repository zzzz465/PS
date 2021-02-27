function reverse(x: number): number {
    const isNegative = x < 0;
    const str = String(x)
    let reversedStr = ''
    if (isNegative) {
        reversedStr = str.split('-')[1].split('').reverse().join('')
    } else {
        reversedStr = str.split('').reverse().join('')
    }
    
    let maxInt = 0
    for (let i = 0; i < 30; i++) {
        maxInt = maxInt | 1
        maxInt = maxInt << 1
    }
    
    const maxStr = String(maxInt)
    
    if (reversedStr.length > maxStr.length || (reversedStr.length == maxStr.length && reversedStr > maxStr)) {
        return 0
    } else {
        if (isNegative)
            return -Number(reversedStr)
        else
            return Number(reversedStr)
    }
};