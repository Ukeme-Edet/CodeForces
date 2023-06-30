const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
let lines = [];
rl.on("line", (line) => lines.push(line));
let currentLine = 0;
const input = () => lines[currentLine++];
rl.on("close", () => {
    let n = parseInt(input());
    let a = input().split(" ").map(Number);
    let max_sub = 1,
        curr_count = 1;
    for (let i = 1; i < n; i++) {
        if (a[i] >= a[i - 1]) curr_count++;
        else {
            max_sub = Math.max(curr_count, max_sub);
            curr_count = 1;
        }
    }
    max_sub = Math.max(curr_count, max_sub);
    console.log(max_sub);
});
