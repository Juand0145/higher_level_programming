#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let movies = 0;

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          ++movies;
        }
      }
    }
    console.log(movies);
  }
});
