function insertion_sort(array: number[]): void {
    for (let i = 1; i < array.length; i++) {
        let val = array[i]
        let index = i - 1

        while ((index >= 0) && array[index] > val) {
            array[index + 1] = array[index]
            index -= 1
        }

        array[index + 1] = val
    }
}

const array = [5, 4, 1, 3, 2]

insertion_sort(array)

console.log(array)

// 나 이거 왜케 헷갈리냐

// https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%EC%82%BD%EC%9E%85%20%EC%A0%95%EB%A0%AC(Insertion%20Sort).md

// 최악의 경우 O(N^2)
// 최선의 경우 O(N) (정렬되어 있을 경우)

export const val = 10