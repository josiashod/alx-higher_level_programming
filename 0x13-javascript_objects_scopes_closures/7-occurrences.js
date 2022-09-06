#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach(el => {
    if (el === searchElement) { occ++; }
  });
  return (occ);
};
