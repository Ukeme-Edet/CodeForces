"""
@file: 2075b_ar.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Array Recoloring(https://codeforces.com/contest/2075/problem/B)
@version: 1.0
@date: 2025-03-17

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        _, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        print(
            sum(sorted(a, reverse=True)[: k + 1])
            if k > 1
            else max(a[0] + max(a[1:]), a[-1] + max(a[:-1]))
        )


if __name__ == "__main__":
    main()
