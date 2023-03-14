package main

import "fmt"

func main() {
	fmt.Println("Hello, world")

	var whatToSay string
	var i int

	whatToSay = "good bye, cruel world"
	fmt.Println(whatToSay)

	i = 7

	fmt.Println("i is set to", i)
 
	// saySomething() //아래 불러오기

	whatWasSaid, theOtherThingThatWasSaid := saySomething()

	fmt.Println("The function returned", whatWasSaid, theOtherThingThatWasSaid)
}

func saySomething() (string, string) {
	return "something", "else"
}
