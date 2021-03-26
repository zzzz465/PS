package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	A, B := readAB()

	if A < B {
		fmt.Println("<")
	} else if A > B {
		fmt.Println(">")
	} else {
		fmt.Println("=")
	}
}

func readAB() (int, int) {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	strs := strings.Split(input, " ")
	first := strs[0]
	second := strings.TrimSuffix(strs[1], "\n")
	a, _ := strconv.Atoi(first)
	b, _ := strconv.Atoi(second)

	return a, b
}
