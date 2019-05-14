#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log('code: ' + response.statusCode);
  }
  let results = JSON.parse(body)['results'];
  let apperances = 0;
  let character = 'https://swapi.co/api/people/18/';
  for (let num in results) {
    if (results[num]['characters'].includes(character)) {
      apperances += 1;
    }
  }
  console.log(apperances);
});
