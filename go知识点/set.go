package main

import (
	"k8s.io/kubernetes/install/go/src/fmt"
	"k8s.io/kubernetes/staging/src/k8s.io/apimachinery/pkg/util/sets"
)

type HashSet struct {
	m map[interface{}]bool
}

// create new set
func NewHashSet() *HashSet {
	return &HashSet{m: make(map[interface{}]bool)}
}

// add set
func (set *HashSet) Add(e interface{}) bool {
	if !set.m[e] {
		set.m[e] = true
		return true
	}
	return false
}

// remove set
func (set *HashSet) Remove(e interface{}) {
	delete(set.m, e)
}

// clear set
func (set *HashSet) Clear() {
	set.m = make(map[interface{}]bool)
}

// contains set
func (set *HashSet) Contains(e interface{}) bool {
	return set.m[e]
}

// set length
func (set *HashSet) Len() int {
	return len(set.m)
}

// tow hashset type is not same
func (set *HashSet) Same(other *HashSet) bool {
	if other == nil {
		return false
	}
	if set.Len() != other.Len() {
		return false
	}
	for key := range set.m {
		if !other.Contains(key) {
			return false
		}
	}
	return true
}

//set is other super set not
func (set *HashSet) IsSuperset(other *HashSet) bool {
	if other == nil {
		return false
	}
	onelen := set.Len()
	otherlen := other.Len()
	if onelen == 0 || onelen == otherlen {
		return false
	}
	if onelen > 0 && otherlen == 0 {
		return true
	}
	//for _, v := range other.Elements() {
	//	if !set.Contains(v) {
	//		return false
	//	}
	//}
	return true
}

func main() {

	set := sets.String{}
	set.Insert("a")
	set.Insert("a")
	fmt.Println(set.List())
}
