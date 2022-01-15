package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
- 점 P1, P2, P3 가 주어진다. (x, y)
- 3 선을 이었을 때, 시계방향인지 구하시오 (P1 -> P2 -> P3) 일 때
- x, y 범위는 -1만 ~ +1만, 정수임
- P1, P2, P3 는 절대 서로 일치하지 않음

- 외적
*/

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var P1_x, P1_y, P2_x, P2_y, P3_x, P3_y int

	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d %d", &P1_x, &P1_y)
	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d %d", &P2_x, &P2_y)
	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d %d", &P3_x, &P3_y)

	vec1_x := P2_x - P1_x
	vec1_y := P2_y - P1_y

	vec2_x := P3_x - P2_x
	vec2_y := P3_y - P2_y

	// 외적
	val := vec1_x * vec2_y - vec1_y * vec2_x

	if val > 0 {
		fmt.Println(1)
	} else if val == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(-1)
	}
}
