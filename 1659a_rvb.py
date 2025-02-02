"""
@file: 1659a_rvb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Red Versus Blue(https://codeforces.com/problemset/problem/1659/A)
@version: 1.0
@date: 2025-02-02

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, r, b = [int(x) for x in input().split()]
        mar = (r + b) // (b + 1)
        mir = r // (b + 1)
        xc = r - (b + 1) * mir
        res = ("R" * mir + "B") * (b - xc + 1) + ("R" * mar + "B") * xc
        print(res[:n])


if __name__ == "__main__":
    main()
