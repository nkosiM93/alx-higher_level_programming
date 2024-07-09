#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let rect = '';
      if (this.width) {
        for (let i = this.height; i > 0; i--) {
          for (let j = this.width; j > 0; j--) {
            rect += c;
          }
          console.log(rect);
          rect = '';
        }
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
