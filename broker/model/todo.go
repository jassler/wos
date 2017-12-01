package model

import "time"

// Todo describes an objective that has to be reached
// until a given due date
type Todo struct {
	Name      string    `json:"name"`
	Completed bool      `json:"completed"`
	Due       time.Time `json:"due"`
}
