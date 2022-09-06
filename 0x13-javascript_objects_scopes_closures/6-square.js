#!/usr/bin/node
const Rectangle = require('./5-rectangle');
module.exports = class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
    }
  }
};
