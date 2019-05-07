#!/usr/bin/node
function factorial (f) {
  if (isNaN(f) || f === 1) {
    return 1;
  }
  return (f * factorial(f - 1));
}
let toFactorial = parseInt(process.argv[2]);
console.log(factorial(toFactorial));
