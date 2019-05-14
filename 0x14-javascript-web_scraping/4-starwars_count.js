#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log('code: ' + response.statusCode);
  }
  let results = JSON.parse(body)['results'];
  let apperances = 0;
  for (let num in results) {
    for (let chars in results[num]['characters']) {
      if (results[num]['characters'][chars].includes('18')) {
        apperances += 1;
      }
    }
  }
  console.log(apperances);
});
