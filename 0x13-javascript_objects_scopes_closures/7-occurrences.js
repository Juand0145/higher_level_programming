#!/usr/bin/node

// Is a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (const element in list) {
    if (list[element] === searchElement) {
      counter++;
    }
  }

  return counter;
};
