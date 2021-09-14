#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const userTask = {};

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (userTask[task.userId]) {
          userTask[task.userId]++;
        } else {
          userTask[task.userId] = 1;
        }
      }
    }
    console.log(userTask);
  }
});
