#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const sliced = process.argv.slice(2, process.argv.length);
  sliced.sort((a, b) => a - b);
  console.log(sliced[sliced.length - 2]);
}
