#!/usr/bin/node
module.exports = class Square {
  constructor (s) {
    if (s > 0) {
      this.size = s;
    }
  }

  print () {
    for (let i = 0; i < this.size; i++) { console.log('X'.repeat(this.size)); }
  }

  double () {
    this.size *= 2;
  }
};
