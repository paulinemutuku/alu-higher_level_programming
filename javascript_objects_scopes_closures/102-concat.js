#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const fileA = fs.readFileSync(args[0]);
const fileB = fs.readFileSync(args[1]);
const fileC = `${fileA}${fileB}`;
fs.writeFileSync(args[4], fileC, (err) => {
  if (err) {
    console.log(err);
  }
});
