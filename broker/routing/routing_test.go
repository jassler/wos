package routing

import (
	"broker/model"
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/gorilla/mux"
)

func TestUsersGet(t *testing.T) {

	// setup
	users := []model.User{
		{ID: "1", Firstname: "John", Lastname: "Doe", Address: &model.Address{City: "City X", State: "State X"}},
		{ID: "2", Firstname: "Koko", Lastname: "Doe", Address: &model.Address{City: "City Z"}},
		{ID: "3", Firstname: "Francis", Lastname: "Sunday"},
	}

	router := NewRouter(&users)

	simulateRequest(t, router, "/users/1", http.StatusOK, fmt.Sprint(`{"id":"1","firstname":"John","lastname":"Doe","address":{"city":"City X","state":"State X"}}`, "\n"))
	simulateRequest(t, router, "/users/2", http.StatusOK, fmt.Sprint(`{"id":"2","firstname":"Koko","lastname":"Doe","address":{"city":"City Z"}}`, "\n"))
	simulateRequest(t, router, "/users/3", http.StatusOK, fmt.Sprint(`{"id":"3","firstname":"Francis","lastname":"Sunday"}`, "\n"))
	simulateRequest(t, router, "/users/4", http.StatusOK, "{}\n")
}

func simulateRequest(t *testing.T, router *mux.Router, url string, expectedStatus int, expectedBody string) {
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()

	// call method and check response
	router.ServeHTTP(rr, req)

	if status := rr.Code; status != expectedStatus {
		t.Errorf("Handler returned wrong status code: got \"%v\" want \"%v\"", status, expectedStatus)
	}

	if rr.Body.String() != expectedBody {
		t.Errorf("handler returned unexpected body: got \"%v\" want \"%v\"", rr.Body.String(), expectedBody)
	}
}
