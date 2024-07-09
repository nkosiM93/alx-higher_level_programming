#!/usr/bin/node

exports.converter = function (base) {
  function convert (quot) {
    if (quot === 0) {
      return 0;
    }
    if (quot < base) {
      return (quot % base).toString(base);
    }
    return convert(Math.floor(quot / base)) + (quot % base).toString(base);
  }
  return convert;
};
