package main

import (
	"broker/model"
	"broker/routing"
	"flag"
	"fmt"
	"log"
	"net/http"
)

func main() {
	// parsing command line arguments
	flag.String("host", "127.0.0.1", "Host address")
	port := flag.Int("port", 8080, "Port")
	flag.Bool("debug", false, "Enable debug mode")

	flag.Parse()

	// dummy todos
	users := []model.User{
		{ID: "1", Firstname: "John", Lastname: "Doe", Address: &model.Address{City: "City X", State: "State X"}},
		{ID: "2", Firstname: "Koko", Lastname: "Doe", Address: &model.Address{City: "City Z", State: "State Y"}},
		{ID: "3", Firstname: "Francis", Lastname: "Sunday"},
	}

	router := routing.NewRouter(&users)

	log.Fatal(http.ListenAndServe(fmt.Sprint(":", *port), router))
}
