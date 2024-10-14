"""
@file: 2025a_ts.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Two Screens(https://codeforces.com/contest/2025/problem/A)
@version: 1.0
@date: 2024-10-14

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
        s, t = sorted([input(), input()], key=len)
        i = 0
        while i < len(s) and s[i] == t[i]:
            i += 1
        print(len(s) + len(t) - len(s[:i]) + (1 if i else 0))


if __name__ == "__main__":
    main()
