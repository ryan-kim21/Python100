package main

import "fmt"

func main() {
	fmt.Println("Hello, world.")

	var whatToSay string
	var i int

	whatToSay = "goodbye, cruel"
	fmt.Println(whatToSay)

	i = 7

	fmt.Println("i is set to", i)

	watWasSaid := saySometing()

	fmt.Println("The function returned", watWasSaid)
}

func saySometing() string {
	return "someting"
}
