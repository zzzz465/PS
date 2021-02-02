function bubble_sort(array: number[]): void {
    for (let i = 0; i < array.length; i++)
        for (let j = 0; j < array.length - i - 1; j++)
            if (array[j] > array[j+1]) {
                const temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            }
}


const arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubble_sort(arr)

console.log(arr)

export const val = 10


// https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%EA%B1%B0%ED%92%88%20%EC%A0%95%EB%A0%AC(Bubble%20Sort).md
/*
장점
구현이 간단하고 소스코드가 직관적이다.
이미 정렬된 데이터를 정렬할 때, 가장 빠르다.
정렬하고자 하는 배열 안에서 정렬하는 방식이므로, 다른 메모리 공간을 필요로 하지 않는다.
안정 정렬이다.
단점
시간 복잡도가 최악, 최선, 평균 모두 O(N^2)이므로 비효율적이다.
다른 정렬에 비해 정렬 속도가 느리다.
교환 횟수가 많다.
역순배열을 정렬할 때, 가장 느리다.
*/