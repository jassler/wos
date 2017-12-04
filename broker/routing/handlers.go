package routing

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

// Index displays welcome message
func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "There are ", len(*users), " users")
}

// UserIndex shows all users in our database
// '/users'
func UserIndex(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(users)
}

// UserShow only shows todo with specified id
// eg. '/users/1'
func UserShow(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	userID, ok := vars["userID"]

	if !ok {
		fmt.Fprintln(w, "No valid ID provided!")
		return
	}

	for _, user := range *users {
		if user.ID == userID {
			// user found!
			json.NewEncoder(w).Encode(user)
			return
		}
	}

	fmt.Fprintln(w, "{}")
}
