#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
add(Number(args[2]), Number(args[3]));
