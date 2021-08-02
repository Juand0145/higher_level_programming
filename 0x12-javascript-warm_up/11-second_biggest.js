#!/usr/bin/node

// Is a script that searches the second biggest integer in the list of arguments.
let numbers = process.argv;
let secondBiggest = 0;
numbers = numbers.sort();

if (numbers.length > 3) {
  secondBiggest = numbers[numbers.length - 2];
}

console.log(secondBiggest);
