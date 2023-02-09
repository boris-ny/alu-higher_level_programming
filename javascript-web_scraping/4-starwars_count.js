#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, body) => {
    if (error) { console.log(error); }
    console.log(JSON.parse(body).results.filter(e1 =>.e1.characters.find(character => character.includes('18'))).length);
});