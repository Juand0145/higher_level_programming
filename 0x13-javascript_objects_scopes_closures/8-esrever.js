#!/usr/bin/node

// Is a function that returns the reversed version of a list
exports.esrever = function (list) {
  const array = [];

  for (const element in list) {
    array.unshift(list[element]);
  }
  return array;
};
