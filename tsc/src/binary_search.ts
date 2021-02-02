function binary_search(array: number[], val: number, start: number, end: number): number {
    if (start < end) {
        const mid = Math.floor((start + end) / 2)
        const midVal = array[mid]

        if (midVal > val)
            return binary_search(array, val, start, mid - 1)
        else if (midVal < val)
            return binary_search(array, val, mid + 1, start)
        else
            return mid
    } else {
        return -1
    }
}

const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

const index = binary_search(array, 5, 0, array.length - 1)
const indexVal = array[index]
console.log(indexVal)

export const val = 10