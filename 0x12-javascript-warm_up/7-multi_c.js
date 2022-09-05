#!/usr/bin/node
const argv = process.argv;
const myNumber = Number.parseInt(argv[2]);

if (!myNumber) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNumber; i++) {
    console.log('C is fun');
  }
}
