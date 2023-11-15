#!/usr/bin/node

const ind = parseInt(Number(process.argv[2]));
if (!isNaN(ind)) {
  for (let b = 0; b < ind; b++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
