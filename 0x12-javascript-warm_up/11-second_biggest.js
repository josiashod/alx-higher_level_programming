#!/usr/bin/node
let argv = process.argv.slice(2);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  argv = argv.map(Number).sort((a, b) => a - b).reverse();
  console.log(argv[1]);
}
