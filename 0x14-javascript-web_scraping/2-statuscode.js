#!/usr/bin/node
const request = require('request');
const link = process.argv[2];

request(link, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
