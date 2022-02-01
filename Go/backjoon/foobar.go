package main

import (
	"encoding/json"
	"log"
)

type Foo struct {
	FooField string
}

type Bar struct {
	BarField string
}

func (b *Bar) BarFunc() {
	b.BarField = "modified"
}

type FooBar struct {
	*Foo
	Bar

	FooBarField string `json:"foobarField2"`
}

func main() {
	foobar := FooBar{}

	foobar.Foo = &Foo{}
	foobar.Bar = Bar{}

	foobar.FooField = "fooValue"
	foobar.BarField = "barValue"
	foobar.FooBarField = "foobarValue"

	foobar.BarFunc()

	b, err := json.Marshal(foobar)
	if err != nil {
		panic(err)
	}

	log.Println(string(b))
}
