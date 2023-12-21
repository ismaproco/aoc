const fs = require("node:fs");

try {
  const data = fs.readFileSync("./input.txt", "utf8");
  let total = 0;
  data.split("\n").forEach((line) => {
    found = line
      .replace("\n", "")
      .split("")
      .filter((char) => !isNaN(char));
    total += parseInt(found[0] + found[found.length - 1]);
  });
  console.log(total);
} catch (err) {
  console.error(err);
}
