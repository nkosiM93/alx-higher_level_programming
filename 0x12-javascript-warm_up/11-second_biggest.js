#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  let sliced = process.argv.slice(2);
  sliced = sliced.sort(function (a, b) {
    return a - b;
  });
  console.log(sliced[sliced.length - 2]);
}
