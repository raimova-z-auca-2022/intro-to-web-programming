// Lab 1: Handling Invalid JSON Parsing
// Task: Write a function to parse JSON and handle errors if parsing fails.

function parseJSON(jsonStr) {
  try {
    let parsedObject = JSON.parse(jsonStr);
    console.log("Parsed object: ", parsedObject);
  } catch (error) {
    console.error("Invalid JSON format");
  }
}

// Example input
parseJSON('{"name": "Alice", "age": 25}');  // Valid JSON
parseJSON('{"name": "Alice", "age": }');    // Invalid JSON

// Lab 2: Debugging with console.log()
// Task: Find and log the sum of all even numbers in an array.

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  console.log("Current number: ", numbers[i]);  // Log each number
  if (numbers[i] % 2 === 0) {
    sum += numbers[i];  // Add even numbers to sum
  }
}

console.log("Sum of even numbers: ", sum);  // Expected Output: 30

// Lab 3: Debugging an Object Array with console.table()
// Task: Create an array of user objects and log it using console.table().

let users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 35 }
];

console.table(users);  // This will display the user data in a table format

// Lab 4: Handling Division Errors
// Task: Write a function that divides two numbers and handles division by zero.

function divide(a, b) {
  try {
    if (b === 0) {
      throw new Error("Cannot divide by zero");
    }
    let result = a / b;
    return result;
  } catch (error) {
    console.error(error.message);  // Expected Output: "Cannot divide by zero"
  }
}

console.log(divide(10, 2));  // Expected Output: 5
console.log(divide(10, 0));  // Expected Output: Error message

// Lab 5: Debugging an Undefined Variable
// Task: Try to access an undefined variable and handle the error.

let someVariable;

try {
  console.log(someVariable);  // Trying to log an undefined variable
} catch (error) {
  console.error("Variable is not defined");  // Expected Output: "Variable is not defined"
}
