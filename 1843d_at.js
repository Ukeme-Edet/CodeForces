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
    let t = parseInt(input());
    let tree, leaf_count;
    for (let i = 0; i < t; i++) {
        let n = parseInt(input());
        tree = new Array(n).fill(0).map(() => []);
        for (let j = 0; j < n - 1; j++) {
            let [u, v] = input().split(" ").map(Number);
            tree[--u].push(--v);
            tree[v].push(u);
        }
        leaf_count = Array(n).fill(0);
        let stack = [[0, 0, -1]];
        while (stack.length) {
            let [node, visit_count, parent] = stack.pop();
            if (visit_count === 0) {
                stack.push([node, 1, parent]);
                for (let child of tree[node]) {
                    if (child !== parent) {
                        stack.push([child, 0, node]);
                    }
                }
            } else {
                if (tree[node].length === 1 && tree[node][0] === parent) {
                    leaf_count[node] = 1;
                } else {
                    for (let child of tree[node]) {
                        if (child !== parent) {
                            leaf_count[node] += leaf_count[child];
                        }
                    }
                }
            }
        }
        let q = parseInt(input());
        for (let j = 0; j < q; j++) {
            let [x, y] = input().split(" ").map(Number);
            console.log(leaf_count[--x] * leaf_count[--y]);
        }
    }
    rl.close();
});

let currentLine = 0;
function input() {
    return lines[currentLine++];
}
