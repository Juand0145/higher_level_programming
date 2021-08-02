#!/usr/bin/node

// Is a script that prints a message depending of the number of arguments passed
const numberOfArguments = process.argv.length;

if (numberOfArguments <= 2) {
  console.log('No argument');
} else if (numberOfArguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
