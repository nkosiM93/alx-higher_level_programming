#!/usr/bin/node

let ind = 0;
while (process.argv[ind]) {
  if (ind === 2) {
    console.log(process.argv[ind]);
    break;
  }
  ind++;
}
console.log('No argument');
