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
	fmt.Println(A - B)
}

func readAB() (int, int) {
	textReader := bufio.NewReader(os.Stdin)
	text, _ := textReader.ReadString('\n')
	splitted := strings.Split(strings.TrimSuffix(text, "\n"), " ")
	A, _ := strconv.Atoi(splitted[0])
	B, _ := strconv.Atoi(splitted[1])

	return A, B
}
