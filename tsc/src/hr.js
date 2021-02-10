function countInversions(arr) {
    let counter = new Array(16)
    counter.fill(0)

    for (const val of arr)
        counter[val]++

    let inversionsCount = 0

    for (let i = 0; i < arr.length; i++) {
        let lower = 0
        for (let j = 0; j < i; j++) {
            if (arr[j] < arr[i])
                lower++
        }

        let required = 0
        for (let j = 1; j < arr[i]; j++)
            required += counter[j]

        if (required - lower > 0)
            inversionsCount += required - lower
    }

    return inversionsCount
}

console.log(countInversions([2, 1, 3, 1, 2]))