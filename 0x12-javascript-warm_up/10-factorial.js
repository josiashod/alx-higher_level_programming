#!/usr/bin/node
const argv = process.argv;

const factorial = (n) => {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
};

console.log(factorial(Number.parseInt(argv[2])));
