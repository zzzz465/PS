package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	A, _ := reader.ReadString('\n')
	B, _ := reader.ReadString('\n')
	A = strings.TrimSuffix(A, "\n")
	B = strings.TrimSuffix(B, "\n")

	for i := len(B) - 1; i >= 0; i-- {
		val := (int)(B[i] - '0')
		a, _ := strconv.Atoi(A)
		fmt.Println(a * val)
	}
}
