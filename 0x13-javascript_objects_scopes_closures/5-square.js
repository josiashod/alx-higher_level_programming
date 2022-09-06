#!/usr/bin/node
module.exports = class Square extends Rectangle {
  constructor (s) {
    super(s, s)
  }
};
