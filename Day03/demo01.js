const s1 = {} // JS Object -> Empty Object
s1.name = "Anil" // Properties
s1.age = 35 // properties
console.log(`type of(s1) - ${typeof (s1)}`)
console.log(s1)

const s2 = {}
s2.name = "Mukesh"
s2.age = 40
s2.mobile = "9876543210"
console.log(s2)

const s3 = {}
s3["first name"] = "Ramesh"
s3.last_name = "Ambani"
console.log(s3)

const s4 = {}
s4["name"] = "Suresh"
s4["age"] = 45
console.log(s4)

// JSON Syntax
const s5 = {
    // properties defined the the form of
    // key(String) : value (number/boolen/string/object/array/function)
    "name": "Ram",
    "age": 50,
    "canVote": true,
    skills: ["C", "CPP", "Java"]
}

s5.mobile = "8976543210"
s5["email Id"] = "ram@gmail.com"
s5.canVote = false
console.log(s5)