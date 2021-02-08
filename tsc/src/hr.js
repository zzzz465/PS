function countTriplets(arr, r) { // number[], number
    const map = new Map()
    for (const val of arr) {
        if (!map.has(val))
            map.set(val, 0)
        
        map.set(val, map.get(val) + 1)
    }

    const keys = [...map.keys()]

    function findTriplets(key) {
        let result = map.get(key)
        let nextValue = key * r
        let found = true
        for (let i = 1; i < 3; i++) {
            if (map.has(nextValue)) {
                result *= map.get(nextValue)
                nextValue *= r
            } else {
                found = false
                break
            }
        }

        if (found)
            return result
        else
            return 0
    }

    let totalCount = 0
    for (const key of keys)
        totalCount += findTriplets(key)

    return totalCount
}

console.log(countTriplets([1, 5, 5, 25, 125], 5))