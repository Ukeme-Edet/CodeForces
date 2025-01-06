"""
@file: 1807g2_sa.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Subsequence Addition (Hard Version)(https://codeforces.com/problemset/problem/1807/G2)
@version: 1.0
@date: 2025-01-06

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        c = sorted([int(x) for x in input().split()])
        cs = c[0]
        for i in range(1, n):
            if cs < c[i]:
                print("NO")
                break
            cs += c[i]
        else:
            print("YES" if c[0] == 1 else "NO")


if __name__ == "__main__":
    main()
