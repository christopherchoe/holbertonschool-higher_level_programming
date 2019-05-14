#!/usr/bin/node
let fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
