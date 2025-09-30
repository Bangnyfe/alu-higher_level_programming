#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < process.argv.length; i++) {
    numbers.push(parseInt(process.argv[i]));
  }
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
