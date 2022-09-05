#!/usr/bin/node
const argv = process.argv;
const number = Number.parseInt(argv[2]);

const factorial = (number) => {
  if (!number || number === 0 || number === 1) { return (1); }
  return (number * factorial(number - 1));
};

console.log(factorial(number));
