#!/usr/bin/node
const txt = 'C is fun';
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log(txt);
  }
}
