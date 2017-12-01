package routing

import (
	"broker/model"
	"net/http"

	"github.com/gorilla/mux"
)

// Route specifies the name, method and pattern it can be called with
type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

var todos *[]model.Todo

// NewRouter adds all items in the routes array to a mux Router
func NewRouter(listTodos *[]model.Todo) *mux.Router {
	todos = listTodos

	router := mux.NewRouter().StrictSlash(true)
	for _, route := range routes {
		router.
			Methods(route.Method).
			Name(route.Name).
			Path(route.Pattern).
			Handler(route.HandlerFunc)
	}

	return router
}

var routes = []Route{
	{
		"Index",
		"GET",
		"/",
		Index,
	},
	{
		"TodoIndex",
		"GET",
		"/todos",
		TodoIndex,
	},
	{
		"TodoShow",
		"GET",
		"/todos/{todoId}",
		TodoShow,
	},
}
