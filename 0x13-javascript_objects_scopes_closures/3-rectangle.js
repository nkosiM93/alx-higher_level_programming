#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    if (this.width) {
      for (let i = this.height; i > 0; i--) {
        for (let j = this.width; j > 0; j--) {
          rect += 'X';
        }
        console.log(rect);
        rect = '';
      }
    }
  }
}
module.exports = Rectangle;
