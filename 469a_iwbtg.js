"use strict";
const readline = require("readline");
let rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});
let lines = [];
rl.on("line", (line) => {
    lines.push(line);
});
rl.on("close", () => {
    let n = parseInt(input());
    let x = input().split(" ").map(Number);
    let y = input().split(" ").map(Number);
    console.log(
        `${
            new Set(x.slice(1).concat(y.slice(1))).size === n
                ? "I become the guy."
                : "Oh, my keyboard!"
        }`
    );
    rl.close();
});
let currentLine = 0;
function input() {
    return lines[currentLine++];
}
