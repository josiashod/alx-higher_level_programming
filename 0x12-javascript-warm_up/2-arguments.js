#!/usr/bin/node
const argv = process.argv;
if (argv.length > 0) {
  console.log(`Argument${argv.length > 3 ? 's' : ''} found`);
} else {
  console.log('No argument');
}
