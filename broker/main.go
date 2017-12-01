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
	todos := []model.Todo{
		{Name: "Code stuff"},
		{Name: "Fix bugs"},
		{Name: "Go shopping"},
	}

	router := routing.NewRouter(&todos)

	log.Fatal(http.ListenAndServe(fmt.Sprint(":", *port), router))
}
