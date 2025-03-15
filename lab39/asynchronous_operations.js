// Lab 1: Understanding Synchronous vs Asynchronous Code
console.log("Start");

setTimeout(() => {
  console.log("Inside setTimeout");
}, 2000);

console.log("End");
// Expected Output:
// Start
// End
// Inside setTimeout (after 2 seconds)

// Lab 2: Using setTimeout to Delay Execution
function delayedMessage(message, delay) {
  setTimeout(() => {
    console.log(message);
  }, delay);
}

delayedMessage("Hello, after 3 seconds!", 3000);
// Expected Output (after 3 seconds):
// Hello, after 3 seconds!

// Lab 3: setInterval to Execute Code Repeatedly
function startCounter() {
  let counter = 1;
  const intervalId = setInterval(() => {
    console.log(`Counter: ${counter}`);
    counter++;
    if (counter > 5) {
      clearInterval(intervalId);
    }
  }, 1000);
}

startCounter();

// Lab 4: Simulating a Delayed API Request Using Promises
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data received");
    }, 2000);
  });
}

fetchData()
  .then((result) => {
    console.log(result); // Expected Output (after 2 seconds): Data received
  })
  .finally(() => {
    console.log("Request completed"); // Expected Output (after 2 seconds): Request completed
  });

// Lab 5: Handling Errors with Promises
function fetchDataWithError() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (Math.random() > 0.5) {
        resolve("Data received");
      } else {
        reject("Error: Failed to fetch data");
      }
    }, 2000);
  });
}

fetchDataWithError()
  .then((result) => {
    console.log(result); // If successful: Data received
  })
  .catch((error) => {
    console.error(error); // If failed: Error: Failed to fetch data
  })
  .finally(() => {
    console.log("Request completed");
  });
