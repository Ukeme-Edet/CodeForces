"""
@file: 1178b_wowf.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem WOW Factor(https://codeforces.com/problemset/problem/1178/B)
@version: 1.0
@date: 2025-01-16

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s = input()
    n = len(s)
    pc = [0] * n
    for i in range(1, n):
        pc[i] = pc[i - 1] + (s[i] == "v" and s[i - 1] == "v")
    res = 0
    for i in range(n):
        if s[i] == "o":
            res += pc[i] * (pc[n - 1] - pc[i])
    print(res)


if __name__ == "__main__":
    main()
