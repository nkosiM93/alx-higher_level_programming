#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let limit = x;
  while (limit > 0) {
    theFunction();
    limit--;
  }
};
