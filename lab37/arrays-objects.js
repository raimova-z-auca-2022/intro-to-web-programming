// Lab 1: Array Methods (push, pop)

// Task: Create an empty array and manipulate it using push() and pop()
let fruits = [];
fruits.push("apple", "banana", "cherry");
console.log("After push: ", fruits);  // Expected: ["apple", "banana", "cherry"]

let removedFruit = fruits.pop();
console.log("Removed element: ", removedFruit);  // Expected: "cherry"
console.log("Final array: ", fruits);  // Expected: ["apple", "banana"]

// Lab 2: Extracting Elements with slice()

// Task: Extract a portion of the array using slice()
let numbers = [10, 20, 30, 40, 50];
let slicedNumbers = numbers.slice(1, 4);  // Extract from index 1 to 3
console.log("Sliced array: ", slicedNumbers);  // Expected: [20, 30, 40]
console.log("Original array: ", numbers);  // Expected: [10, 20, 30, 40, 50]

// Lab 3: Transforming Data with map()

// Task: Square each number in the array using map()
let nums = [1, 2, 3, 4, 5];
let squaredNums = nums.map(num => num * num);
console.log("Original array: ", nums);  // Expected: [1, 2, 3, 4, 5]
console.log("Squared array: ", squaredNums);  // Expected: [1, 4, 9, 16, 25]

// Lab 4: Filtering Data with filter()

// Task: Filter values greater than or equal to 18
let ages = [12, 18, 25, 30, 15];
let adults = ages.filter(age => age >= 18);
console.log("Filtered array: ", adults);  // Expected: [18, 25, 30]

// Lab 5: Working with Objects (Key-Value Operations)

// Task: Create an object and perform operations on it
let user = {
  name: "Alice",
  age: 25,
  city: "New York"
};

console.log("Name: ", user.name);  // Expected: "Alice"

// Update the age property
user.age = 26;
console.log("Updated user: ", user);  // Expected: { name: "Alice", age: 26, city: "New York" }

// Lab 6: Extracting Keys and Values

// Task: Extract keys and values from an object
let car = {
  brand: "Tesla",
  model: "Model S",
  year: 2023
};

let keys = Object.keys(car);
let values = Object.values(car);

console.log("Object keys: ", keys);  // Expected: ["brand", "model", "year"]
console.log("Object values: ", values);  // Expected: ["Tesla", "Model S", 2023]
