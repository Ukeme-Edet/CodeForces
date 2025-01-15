"""
@file: 2025c_tt.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem The Trail(https://codeforces.com/problemset/problem/2025/C)
@version: 1.0
@date: 2025-01-15

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        s = input()
        s += "R" if s[-1] == "D" else "D"
        grid = [[int(x) for x in input().split()] for _ in range(n)]
        csr = [sum(x) for x in grid]
        csc = [sum(x) for x in zip(*grid)]
        x = y = 0
        for i in range(n + m - 1):
            if s[i] == "R":
                grid[x][y] = csc[y] * -1
                csr[x] -= csc[y]
                csc[y] = 0
                y += 1
            else:
                grid[x][y] = csr[x] * -1
                csc[y] -= csr[x]
                csr[x] = 0
                x += 1
        print("\n".join(" ".join(str(x) for x in row) for row in grid))


if __name__ == "__main__":
    main()
