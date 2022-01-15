package main

import (
	"bufio"
	"fmt"
	"os"
)

// 모든 점 과의 거리의 합을 최소로
// 두 위치 거리는 맨해턴 거리로 측정한다
// 좌표의 수는 1개 ~ 10만개
// x, y 좌표의 범위는 -1백만 ~ 1백만

func main() {
	var N int
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d", &N)

	coords := make([][]int, 0)

	for i := 0; i < N; i++ {
		scanner.Scan()

		var x, y int
		fmt.Sscanf(scanner.Text(), "%d %d", &x, &y)

		coords = append(coords, []int{ x, y })
	}

	/*
	2 + 3 = 5 / 2 = 2
	2 + 5 = 7 / 2 = 3
	3 + 1 = 4 / 2 = 2
	2 + -2 = 0 / 2 = 0
	x = 0

	2 + 4 = 6 / 2 = 3
	3 + 6 = 9 / 2 = 4
	4 + 9 = 13 / 2 = 6
	6 + -8 = -2 / 2 = -1
	y = -1

	(2, 2) ~ (0, -1) = 5
	(3, 4) ~ (0, -1) = 5
	(5, 6) ~ (0, -1) = 7
	(1, 9) ~ (0, -1) = 11
	(-2, -8) ~ (0, -1) = 2 + 7 = 9

	5 + 5 + 7 + 11 + 9 = 10 + 7 + 20 = 37
	 */
}
