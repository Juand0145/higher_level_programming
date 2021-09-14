#!/usr/bin/node
const fs = require('fs');
const fileToRead = process.argv[2];

fs.readFile(fileToRead, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
