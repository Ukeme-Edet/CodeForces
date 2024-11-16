"""
@file: 2031b_pass.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Penchick and Satay Sticks(https://codeforces.com/contest/2031/problem/B)
@version: 1.0
@date: 2024-11-17

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = [(int(x), i) for i, x in enumerate(input().split())]
        print(
            "YES"
            if all(abs(p[i][0] - p[i][1] - 1) < 2 for i in range(n))
            else "NO"
        )


if __name__ == "__main__":
    main()
