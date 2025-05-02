"""
@file: 2108c_ne.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Neo's Escape(https://codeforces.com/contest/2108/problem/C)
@version: 1.0
@date: 2025-05-02

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
        a = [int(x) for x in input().split()]
        res = i = inc = 1
        while i < n:
            if (inc and a[i] >= a[i - 1]) or (not inc and a[i] <= a[i - 1]):
                i += 1
            elif inc and a[i] < a[i - 1]:
                inc = 0
                i += 1
            else:
                res += 1
                inc = 1
                i += 1
        print(res)


if __name__ == "__main__":
    main()
