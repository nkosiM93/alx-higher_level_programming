#!/usr/bin/node

let ind = 0;
let first, second;
while (ind < process.argv.length) {
  if (ind === 2) {
    first = process.argv[2];
  }
  if (ind === 3) {
    second = process.argv[3];
    break;
  }
  ind++;
}
console.log(first + ' is ' + second);
