package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, k int
	fmt.Scanf("%d %d", &n, &k)

	weights := make([]int, 0)

	for i := 0; i < n; i++ {
		var input int
		fmt.Scanf("%d", &input)

		weights = append(weights, input)
	}

	sort.Slice()
}
