"""
@file: 1914d_ta.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Three Activities(https://codeforces.com/problemset/problem/1914/D)
@version: 1.0
@date: 2025-01-01

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        _ = int(input())
        res = 0
        a = sorted(
            [(int(x), i) for i, x in enumerate(input().split())], reverse=True
        )
        b = sorted(
            [(int(x), i) for i, x in enumerate(input().split())], reverse=True
        )
        c = sorted(
            [(int(x), i) for i, x in enumerate(input().split())], reverse=True
        )
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if len(set([a[i][1], b[j][1], c[k][1]])) == 3:
                        res = max(res, a[i][0] + b[j][0] + c[k][0])
        print(res)


if __name__ == "__main__":
    main()
