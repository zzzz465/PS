package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

// https://www.acmicpc.net/problem/1034

/*
 1. 2D array (직사각형, 정사각형 아님!!!) 가 있음
 2. 각 상태는 true / false 임
 3. 한 row 가 전부 true 이면, count += 1 임
 4. 한 번의 action 으로 column 의 상태를 invert 할 수 있음
 5. 무조건 K 번 switch 를 눌러야 함
 6. 어떻게 해야 K 번 누른 다음 count 를 최대로 만들 수 있을까?

- 입력 조건 잘 확인해야 함
- 1. 크기는 최대 50x50 까지 가능
- 2. K 번 switch 를 할 수 있는데, 0 <= K <= 1000 (0 포함!!!) 이다.

- 한 column 을 2번 누르면, 원래 상태로 돌아온다.
- 즉, 1개의 column 을 짝수번 누르냐, 홀수번 누르냐가 중요하다.
- column 의 개수를 X 라고 할 때, N <= X 이고, N 번 누르는 경우의 수만 구하면 + 짝수, 홀수일 때만 판단하면 큰 숫자는 필요 X
- 무식한 방법으로 해보기?
- 50개니까 2^50 이면.. 상태가 너무 많지 않나?
- 시간 제한은 2초이므로, 약 2억 번 까지 연산 가능
- 2^50 은 ... 2억 번은 한참 벗어났다.
- 최적화를 할 수 있는가?
- 순서가 정해져있지 않으므로, 임의로 순서를 정해보자.
- 왼쪽부터 차례대로 시작한다고 생각해보자.
- row 로 생각해보면, 아무리 많아봤자 50개의 패턴이 존재하잖아
- 그렇다면, 가장 많은 패턴을 찾아서, 뒤집어주면 되는게 아닐까?
- 2 가지 이상의 패턴을 세어야 하는 경우의 수가 있는가?
*/

var (
	M int
	K int
	N int
) // N 은 세로, M 는 가로
var table [][]int

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	_, _ = fmt.Sscanf(scanner.Text(), "%d %d", &N, &M)

	table = make([][]int, N)

	// read
	for i := 0; i < N; i++ {
		table[i] = make([]int, M)

		scanner.Scan()

		for j, c := range scanner.Text() {
			if c == '1' {
				table[i][j] = 1
			} else {
				table[i][j] = 0
			}
		}
	}

	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "%d", &K)

	solve()
}

func solve() {
	patternsSet := make(map[string]int)

	// count patterns
	for _, line := range table {
		pattern := buildPattern(line)

		patternsSet[pattern] += 1
	}

	type kv struct {
		Key   string
		Value int
	}

	patterns := make([]kv, 0)
	for k, v := range patternsSet {
		patterns = append(patterns, kv{
			Key:   k,
			Value: v,
		})
	}

	// sort patterns
	sort.Slice(patterns, func(i, j int) bool { return patterns[i].Value > patterns[j].Value })

	// 굳이 second 까지 계산 해야하나? 왠지 해야할거 같은데...
	// 할 필요 없겠지?
	// top, second := patterns[0], patterns[1]

	for _, pair := range patterns {
		if canMakeAllOk(pair.Key) {
			fmt.Println(pair.Value)
			return
		}
	}

	fmt.Println("0")
}

func buildPattern(line []int) string {
	chars := make([]string, 0)

	for _, val := range line {
		if val == 1 {
			chars = append(chars, "1")
		} else {
			chars = append(chars, "0")
		}
	}

	return strings.Join(chars, "")
}

// accepts "01010101...101001101"
func canMakeAllOk(line string) bool {
	zeroCount := 0

	for _, c := range line {
		if c == '0' {
			zeroCount += 1
		}
	}

	remaining := zeroCount - K

	if remaining > 0 {
		return false
	} else if remaining == 0 {
		return true
	} else {
		return remaining % 2 == 0
	}
}
