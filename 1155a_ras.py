"""
@file: 1155a_ras.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Reverse a Substring(https://codeforces.com/problemset/problem/1155/A)
@version: 1.0
@date: 2025-02-05

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        if s[i] < s[i - 1]:
            print("YES")
            print(i, i + 1)
            return
    print("NO")


if __name__ == "__main__":
    main()
