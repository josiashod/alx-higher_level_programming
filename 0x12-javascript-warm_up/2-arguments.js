#!/usr/bin/node
const argv = process.argv;
if (argv.length > 2) {
  console.log(`Argument${argv.length > 3 ? 's' : ''} found`);
} else {
  console.log('No argument');
}
