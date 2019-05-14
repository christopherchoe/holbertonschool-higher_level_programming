#!/usr/bin/node
let fs = require('fs');
let toWrite = process.argv[3];
fs.writeFile(process.argv[2], toWrite, function read (err) {
  if (err) {
    console.log(err);
  }
});
