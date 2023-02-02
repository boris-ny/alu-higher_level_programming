#!/usr/bin/node
const myArgs = process.argv.length;
const myArray = [];
switch (myArgs) {
  case 2:
  case 3:
    console.log(0);
    break;
  default:
    for (let i = 2; i < myArgs; i++) {
      myArray.push(process.argv[i]);
    }
    myArray.sort(function (a, b) { return b - a; });
    console.log(myArray[1]);
    break;
}
