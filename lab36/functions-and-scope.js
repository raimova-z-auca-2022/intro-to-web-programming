// Lab 1: Creating Functions

// Task 1: Function using function keyword
function addNumbers(a, b) {
  return a + b;
}
console.log("Sum: ", addNumbers(3, 4));  // Example Output: Sum:  7

// Task 2: Arrow function to calculate square
const square = (x) => x * x;
console.log("Square: ", square(5));  // Example Output: Square:  25

// Task 3: Function expression to return larger of two numbers
const max = function(a, b) {
  return a > b ? a : b;
};
console.log("Larger number: ", max(10, 20));  // Example Output: Larger number:  20

// Lab 2: Local vs Global Scope

// Global variable
let message = "Hello from global";

// Function with local scope
function displayMessage() {
  let message = "Hello from local";  // Local variable
  console.log(message);  // Expected: "Hello from local"
}

// Calling the function
displayMessage();

// Logging global message
console.log(message);  // Expected: "Hello from global"

// Lab 3: Block Scope with let & const

// Task 1: var scope
if (true) {
  var nameVar = "Global Scope";
}
console.log(nameVar);  // Expected: "Global Scope" (accessible outside the block)

if (true) {
  let nameLet = "Block Scope with let";
  const nameConst = "Block Scope with const";
  console.log(nameLet);  // Expected: "Block Scope with let"
  console.log(nameConst);  // Expected: "Block Scope with const"
}

try {
  console.log(nameLet);  // Error: nameLet is not defined
} catch (e) {
  console.log(e.message);  // Expected: nameLet is not defined
}

try {
  console.log(nameConst);  // Error: nameConst is not defined
} catch (e) {
  console.log(e.message);  // Expected: nameConst is not defined
}

// Lab 4: Understanding Closures

// Task 1: Counter function
function counter() {
  let count = 0;  // Private variable
  return function() {
    count++;  // Increment the private variable
    return count;
  };
}

// Task 2: Create two separate counters
const counter1 = counter();
const counter2 = counter();

// Task 3: Calling the counters
console.log("Counter 1: ", counter1());  // Expected: Counter 1: 1
console.log("Counter 1: ", counter1());  // Expected: Counter 1: 2
console.log("Counter 2: ", counter2());  // Expected: Counter 2: 1
console.log("Counter 2: ", counter2());  // Expected: Counter 2: 2
