package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {

	var count int
	
	path := os.Args[1]

	file, err := os.Open(path)
    if err != nil {
        // handle the error here
        return
        } 
    defer file.Close()

	scanner := bufio.NewScanner(file)
	//scan lines of the file
	for scanner.Scan() {
		count++
	}
	fmt.Println(count)
}


