#!/usr/bin/node

if (process.argv.length > 2) {
  if (process.argv[2] !== "" && Number(process.argv[2]) === 'number') {
    console.log('My number: ' + parseInt(Number(process.argv[2])));
  } else {
      console.log('Not a number');
  }
} else {
    console.log('Not a number');
}
