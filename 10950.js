const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];

rl.on("line", function (line) {
  line = line.split(" ");
  input.push(line);
}).on("close", function () {
  input.map((i) => {
    if (i.length > 1) {
      console.log(Number(i[0]) + Number(i[1]));
    }
  });
  process.exit();
});
