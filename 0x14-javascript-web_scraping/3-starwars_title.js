#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log('code: ' + response.statusCode);
  }
  console.log(JSON.parse(body)['title']);
});
