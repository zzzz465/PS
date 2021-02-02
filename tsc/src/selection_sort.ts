import { sortAndDeduplicateDiagnostics } from "typescript"

function selection_sort(array: number[]): void {
    for (let i = 0; i < array.length; i++) {
        let least_index = i
        for (let j = i; j < array.length; j++)
            if (array[j] < array[least_index])
                least_index = j

        const temp = array[i]
        array[i] = array[least_index]
        array[least_index] = temp
    }
}

const array = [5, 4, 3, 1, 2]

selection_sort(array)

console.log(array)

// https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%EC%84%A0%ED%83%9D%20%EC%A0%95%EB%A0%AC(Selection%20Sort).md
// O(N^2)
// 추가 메모리 필요 X