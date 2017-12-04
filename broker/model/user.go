package model

// User type contains a unique ID, a first-/lastname and address
type User struct {
	ID        string   `json:"id,omitempty"`
	Firstname string   `json:"firstname,omitempty"`
	Lastname  string   `json:"lastname,omitempty"`
	Address   *Address `json:"address,omitempty"`
}

// Address contains a city and state
type Address struct {
	City  string `json:"city,omitempty"`
	State string `json:"state,omitempty"`
}
