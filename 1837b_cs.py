"""
@file: 1837b_cs.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Comparison String(https://codeforces.com/problemset/problem/1837/B)
@version: 1.0
@date: 2025-02-07

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        res = i = 1
        while i < n:
            tres = 1
            while i < n and s[i] == s[i - 1]:
                tres += 1
                i += 1
            res = max(res, tres)
            i += 1
        print(res + 1)


if __name__ == "__main__":
    main()
