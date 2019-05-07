#!/usr/bin/node
let i;
let row = '';
let myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (i = 0; i < myNum; i++) {
    row += 'X';
  }
  for (i = 0; i < myNum; i++) {
    console.log(row);
  }
}
