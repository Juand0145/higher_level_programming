#!/usr/bin/node

// Is  a script that prints x times “C is fun”
let number = process.argv[2];
let i = 0;

if (!parseInt(number)) {
  console.log('Missing number of occurrences');
} else {
  number = parseInt(number);
  while (i < number) {
    console.log('C is fun');
    i++;
  }
}
