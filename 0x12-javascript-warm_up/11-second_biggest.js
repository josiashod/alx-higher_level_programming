#!/usr/bin/node
let argv = process.argv.slice(2);

argv = argv.map(e => Number.parseInt(e)).sort().reverse();
if (argv[1]) { console.log(argv[1]); } else { console.log(0); }
