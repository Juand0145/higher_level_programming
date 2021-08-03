#!/usr/bin/node

// Is a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
const firstSquare = require('./5-square');

class Square extends firstSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
