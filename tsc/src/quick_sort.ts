import { textSpanIntersectsWithPosition } from "typescript"

function quick_sort(array: number[], start: number, end: number): void {
    const keyVal = array[Math.floor((start + end) / 2)]
    let low = start
    let high = end

    while (low <= high) {
        while (array[low] < keyVal) low++
        while (array[high] > keyVal) high--

        if (low <= high) {
            if (low != high) {
                const temp = array[low]
                array[low] = array[high]
                array[high] = temp
            }

            low++
            high--
        }
    }

    if (start < high) quick_sort(array, start, high)
    if (low < end) quick_sort(array, low, end)
}


const array = [1,4,5,9,8,0,7,6,3,2]

quick_sort(array, 0, array.length - 1)

console.log(array)