#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/:id/${url}`, (error, response) => {
  if (error) { console.log(error); }
  console.log(JSON.parse(response.body).title);
});
