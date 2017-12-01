package main

import (
	"broker/model"
	"broker/routing"
	"log"
	"net/http"
)

// global todo list we can access in '/todos'
var todos []model.Todo

func main() {

	router := routing.NewRouter()

	log.Fatal(http.ListenAndServe(":8080", router))
}
