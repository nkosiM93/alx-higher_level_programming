#!/usr/bin/node

let count = 0;
process.argv.forEach(function (a) {
  count++;
});

if (count <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
