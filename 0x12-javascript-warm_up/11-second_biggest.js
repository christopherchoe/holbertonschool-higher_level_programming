#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('0');
} else {
  let max = parseInt(process.argv[2]);
  let second = parseInt(process.argv[2]);
  process.argv.forEach((val, index) => {
    if (parseInt(val) > max) {
      second = max;
      max = parseInt(val);
    }
  });
  console.log(second);
}
