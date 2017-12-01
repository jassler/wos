package routing

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

// Index displays welcome message
func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "There are ", len(*todos), " things to be done")
}

// TodoIndex shows all todos from our todo array
// '/todos'
func TodoIndex(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(todos)
}

// TodoShow only shows todo with specified id
// eg. '/todos/1'
func TodoShow(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	todoID, err := strconv.Atoi(vars["todoId"])

	if err != nil {
		fmt.Fprintln(w, "Please provide a number from 0 to ", len(*todos)-1, " to show more")
		return
	}

	if todoID < 0 || todoID >= len(*todos) {
		fmt.Fprintln(w, "Please provide a number from 0 to ", len(*todos)-1, " to show more")
		return
	}

	fmt.Fprintln(w, "Todo: ", (*todos)[todoID])
}
