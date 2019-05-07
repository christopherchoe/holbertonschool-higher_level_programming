#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('0');
} else {
  let max = parseInt(process.argv[2]);
  let second = parseInt(process.argv[2]) > parseInt(process.argv[3])
    ? parseInt(process.argv[3])
    : parseInt(process.argv[2]);
  process.argv.forEach((val, index) => {
    if (parseInt(val) > max) {
      console.log('test' + second + ' ' + max);
      second = max;
      max = parseInt(val);
    } else if (parseInt(val) !== max && parseInt(val) > second) {
      second = parseInt(val);
    }
  });
  console.log(second);
}
