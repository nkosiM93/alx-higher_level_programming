#!/usr/bin/node

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  if (num < 0) {
    return undefined;
  }
  return num * factorial(--num);
}

console.log(factorial(parseInt(process.argv[2])));
