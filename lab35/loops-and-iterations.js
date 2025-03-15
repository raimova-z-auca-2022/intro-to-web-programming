// Lab 1: Using the for Loop
console.log("Lab 1: Using the for Loop");
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// Lab 2: Using the while Loop
console.log("\nLab 2: Using the while Loop");
let num = 10;
while (num >= 1) {
  console.log(num);
  num--;
}

// Lab 3: Using the do...while Loop
console.log("\nLab 3: Using the do...while Loop");
let userInput;
do {
  userInput = parseInt(prompt("Enter a number greater than 10:"));
} while (userInput <= 10);

// Lab 4: Looping Through an Array with for Loop
console.log("\nLab 4: Looping Through an Array with for Loop");
let fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// Lab 5: Looping Through an Array with while Loop
console.log("\nLab 5: Looping Through an Array with while Loop");
let i = 0;
while (i < fruits.length) {
  console.log(fruits[i]);
  i++;
}

// Lab 6: Using break in a Loop
console.log("\nLab 6: Using break in a Loop");
let numbers = [3, 7, 12, 5, 9];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] === 12) {
    console.log("Found 12, stopping the loop.");
    break;
  }
}

// Lab 7: Using continue in a Loop
console.log("\nLab 7: Using continue in a Loop");
let numbers2 = [1, 2, 3, 4, 5, 6, 7];
for (let i = 0; i < numbers2.length; i++) {
  if (numbers2[i] === 5) {
    continue;
  }
  console.log(numbers2[i]);
}


