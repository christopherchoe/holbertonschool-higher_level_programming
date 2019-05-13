#!/usr/bin/node
const prevSquare = require('./5-square');
class Square extends prevSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
      return;
    }
    let row = '';
    let i = 0;
    for (i = 0; i < this.height; i++) {
      row += c;
    }
    for (i = 0; i < this.width; i++) {
      console.log(row);
    }
  }
}
module.exports = Square;
