#!/usr/bin/node
let i;
let myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
