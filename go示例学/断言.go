package main

import (
	"fmt"
)

func classifier(items ...interface{}) {
	for i, x := range items {
		switch x.(type) {
		case int, int8, int16, int32, int64:
			fmt.Println("int ... %d", i)
		case float32, float64:
			fmt.Println("float32 ... %d", i)
		case bool:
			fmt.Println("bool")
		case string:
			fmt.Println("string")
		case nil:
			fmt.Println("nil")
		default:
			fmt.Println("unknown type")

		}
	}
}

func main() {
	classifier(1, true, "a", 1.12)
}
