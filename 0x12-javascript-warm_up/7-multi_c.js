#!/usr/bin/node
const argv = process.argv;
let myNumber = Number.parseInt(argv[2]);

if (!myNumber) {
  console.log('Missing number of occurrences');
} else {
    do {
	console.log('C is fun');
	myNumber--;
    } while(myNumber > 0);
}
