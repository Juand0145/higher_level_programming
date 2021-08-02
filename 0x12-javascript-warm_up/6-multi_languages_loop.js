#!/usr/bin/node

// Is a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
const array = ['C is fun', 'Python is cool', 'Javascript is amazing'];

for (const arg in array) {
  console.log(array[arg]);
}
