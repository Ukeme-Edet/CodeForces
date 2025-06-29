"""
@file: 1900a_ciw.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Cover in Water(https://codeforces.com/problemset/problem/1900/A)
@version: 1.0
@date: 2025-06-29

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
        print(2 if "..." in s else sum(len(x) for x in s.split("#")))


if __name__ == "__main__":
    main()
