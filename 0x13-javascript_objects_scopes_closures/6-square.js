#!/usr/bin/node
const Rectangle = require('./3-rectangle');
module.exports = class Square {
  constructor (s) {
    super(s, s)
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) { console.log(c.repeat(this.width)); }
  }
};
