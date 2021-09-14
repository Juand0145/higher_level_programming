#!/usr/bin/node
const fs = require('fs');
const fileToRead = process.argv[2];
const fileToWrite = process.argv[3];

fs.writeFile(fileToRead, fileToWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
