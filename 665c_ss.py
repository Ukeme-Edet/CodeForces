"""
@file: 665c_ss.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Simple Strings(https://codeforces.com/problemset/problem/665/C)
@version: 1.0
@date: 2025-01-27

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s = [x for x in input()]
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            while s[i] == s[i - 1] or (i < n - 1 and s[i] == s[i + 1]):
                s[i] = chr((ord(s[i]) - 96) % 26 + 97)
    print("".join(s))


if __name__ == "__main__":
    main()
