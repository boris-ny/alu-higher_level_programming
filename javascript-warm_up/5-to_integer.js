#!/usr/bin/node
const firstArgv = parseInt(process.argv[2]);
if (isNaN(firstArgv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArgv);
}
