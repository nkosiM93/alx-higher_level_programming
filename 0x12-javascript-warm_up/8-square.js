#!/usr/bin/node

if (!(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = process.argv[2]; i > 0; i--) {
    let str = '';
    for (let i = process.argv[2]; i > 0; i--) {
      str += 'X';
    }
    console.log(str);
  }
}
