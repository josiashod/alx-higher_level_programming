#!/usr/bin/node
exports.esrever = function (list) {
  const rev = new Array(list.length);
  for (let i = 0; i < list.length; i++) {
    rev[i] = list[list.length - (i + 1)];
  }
  return (rev);
};
