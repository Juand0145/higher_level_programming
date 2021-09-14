#!/usr/bin/node
const request = require('request');
const link = 'http://swapi.co/api/films/' + process.argv[2];

request.get(link,
  function (err, response, body) {
    if (err) console.log(error);
    else console.log(JSON.parse(body).title);
  });
