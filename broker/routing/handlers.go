package routing

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

// Index displays welcome message
func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome")
}

// TodoIndex shows all todos from our todo array
// '/todos'
func TodoIndex(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(todos)
}

// TodoShow only shows todo with specified id
// eg. '/todos/1'
func TodoShow(w http.ResponseWriter, r *http.Request) {
	fmt.Println("hi")
	vars := mux.Vars(r)
	todoId := vars["todoId"]
	fmt.Fprintln(w, "Todo show:", todoId)
}
