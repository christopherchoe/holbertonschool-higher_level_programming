#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = new Array(list.length);
  let i = 0;
  let k = list.length - 1;
  for (i = 0; i < list.length; i++) {
    reverse[k] = list[i];
    k -= 1;
  }
  return reverse;
};
