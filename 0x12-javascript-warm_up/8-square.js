#!/usr/bin/node

// Is a script that prints a square
let number = process.argv[2];

if (!parseInt(number)) {
  console.log('Missing size');
} else {
  number = parseInt(number);

  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
