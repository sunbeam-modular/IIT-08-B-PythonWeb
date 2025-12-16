const arr = [10, 20, 30, 40, 50]
console.log(arr)

console.log("using for of loop")
for (const e of arr)
    console.log(e)

console.log("using forEach()")
// forEach is an higher order function
// it is a method declared inside the array object
arr.forEach(value => console.log(value))

