#!/usr/bin/node
exports.converter = function (base) {
  function converts(num) {
    return parseInt(num).toString(base);
  }
  return converts;
}
