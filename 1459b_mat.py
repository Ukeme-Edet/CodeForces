"""
@file: 1459b_mat.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Move and Turn(https://codeforces.com/problemset/problem/1459/B)
@version: 1.0
@date: 2025-01-02

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    print((n // 2 + 1) * (n // 2 + 2) * 2 if n % 2 else (n // 2 + 1) ** 2)


if __name__ == "__main__":
    main()
