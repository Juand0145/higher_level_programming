#!/usr/bin/node

/*
 Is script that prints My number: <first argument converted in integer>
 if the first argument can be converted to an integer:
*/
const number = process.argv[2];
if (!parseInt(number)) {
  console.log('Not a number');
} else {
  console.log('My number ' + number);
}
