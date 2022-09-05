#!/usr/bin/node
const argv = process.argv;
const size = Number.parseInt(argv[2]);
let string = '';

if (!size) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < size; i++) {
    string += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(string);
  }
}
