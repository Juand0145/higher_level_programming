#!/usr/bin/node
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(link,
  function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
