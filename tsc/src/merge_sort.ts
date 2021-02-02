function merge_sort(array: number[], start: number, end: number): void {
    if (start < end) {
        const mid = Math.floor((start + end) / 2)
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end)
    }
}

function merge(array: number[], start: number, mid: number, end: number) {
    const sorted = new Array(end - start + 1)
    let index = 0
    let left = start
    let right = mid + 1

    while (index <= mid && right <= end)
        if (array[left] < array[right])
            sorted[index++] = array[left++]
        else
            sorted[index++] = array[right++]

    if (left > mid) // mid보다 index가 큰것은, 이제 mid 우측에 남은것들만 합치면 됨
        for (let j = right; j <= end; j++)
            sorted[index++] = array[j]
    else // mid 좌측에 있는 것만 합치면 됨
        for (let j = left; j <= mid; j++)
            sorted[index++] = array[j]

    index = 0
    for (let i = start; i <= end; i++)
        array[i] = sorted[index++]

    return
}

const array = [5, 4, 1, 3, 2]

merge_sort(array, 0, array.length - 1)

console.log(array)

// https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%EB%B3%91%ED%95%A9%20%EC%A0%95%EB%A0%AC(Merge%20Sort).md