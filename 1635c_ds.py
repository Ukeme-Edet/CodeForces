"""
@file: 1635c_ds.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Differential Sorting(https://codeforces.com/problemset/problem/1635/C)
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
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        if a == sorted(a):
            print(0)
            continue
        if a[-1] < a[-2] or a[-2] - a[-1] > a[-2]:
            print(-1)
            continue
        print(n - 2)
        for i in range(n - 2):
            print(f"{i + 1} {n - 1} {n}")


if __name__ == "__main__":
    main()
