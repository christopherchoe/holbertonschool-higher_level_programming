#!/usr/bin/node
let logCalls = 0;
exports.logMe = function (item) {
  console.log(logCalls + ': ' + item);
  logCalls += 1;
};
