"""
@file: 1791g1_teleporters.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Teleporters (Easy Version)(https://codeforces.com/problemset/problem/1791/G1)
@version: 1.0
@date: 2025-01-08

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, c = [int(x) for x in input().split()]
        a = sorted(
            [(int(x), i + 1) for i, x in enumerate(input().split())],
            key=lambda x: sum(x),
        )
        res = 0
        for i in range(n):
            c -= a[i][1] + a[i][0]
            if c < 0:
                break
            res += 1
        print(res)


if __name__ == "__main__":
    main()
