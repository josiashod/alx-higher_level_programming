#!/usr/bin/node
const argv = process.argv;

function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
};

console.log(factorial(Number(argv[2])));
