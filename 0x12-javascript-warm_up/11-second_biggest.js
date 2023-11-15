#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const copyArr = process.argv.slice(2);
  copyArr.sort((a, b) => a - b);
  console.log(copyArr[copyArr.length - 2]);
}
