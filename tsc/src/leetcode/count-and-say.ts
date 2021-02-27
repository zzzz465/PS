function countAndSay(n: number): string {
    if (n == 1)
        return '1'
    
    const recurr = countAndSay(n-1)
    
    const says = []
    
    let currNum = recurr[0]
    let numCount = 1
    for (let i = 1; i < recurr.length; i++) {
        if (currNum !== recurr[i]) {
            says.push([currNum, numCount])
            currNum = recurr[i]
            numCount = 1
        } else {
            numCount += 1
        }
    }
    
    if (numCount > 0) {
        says.push([currNum, numCount])
    }
    
    return says.map(([a, b]) => String(b) + a).join('')
};