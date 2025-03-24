package main

import (
	"fmt"
	"time"
)

func main() {
	manilaLocation, err := time.LoadLocation("Asia/Manila")
	if err != nil {
		fmt.Println("Could not load Manila time zone, using UTC+8 instead")
		manilaLocation = time.FixedZone("UTC+8", 8*60*60)
	}

	manilaTime := time.Now().In(manilaLocation)
	timeString := manilaTime.Format("3:04:05 PM")

	fmt.Println("Hello, Laurence!")
	fmt.Println("The current time in Manila, Philippines is:", timeString)
	fmt.Println("Date:", manilaTime.Format("Monday, January 2, 2006"))

}
