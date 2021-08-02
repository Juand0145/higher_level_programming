#!/usr/bin/node

// Is a script that prints two arguments passed to it, in the following format: “ is ”
const argument1 = process.argv[2];
const argument2 = process.argv[3];

console.log(argument1 + ' is ' + argument2);
