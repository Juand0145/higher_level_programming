#!/usr/bin/node

// Is a script that computes and prints a factorial
function factorial (x) {
  if (x === 0 || NaN || !x) {
    return 1;
  }

  return (x * factorial(x - 1));
}

const number = parseInt(process.argv[2]);
const result = factorial(number);

console.log(result);
