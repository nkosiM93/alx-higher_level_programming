#!/usr/bin/node
exports.esrever = function (list) {
  let newArr = [];
  for (let i = 0; i < list.length; i++) {
    newArr.unshift(list[i]);
  }
  return newArr;
};
