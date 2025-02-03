"""
@file: 1614b_daanp.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Divan and a New Project(https://codeforces.com/problemset/problem/1614/B)
@version: 1.0
@date: 2025-02-03

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
        a = sorted(
            [(int(x), i) for i, x in enumerate(input().split())], reverse=True
        )
        res = [0] * (n + 1)
        d = 1
        td = 0
        for i in range(n):
            res[a[i][1] + 1] = d
            td += abs(d) * 2 * a[i][0]
            if d < 0:
                d = -d + 1
            else:
                d = -d
        print(td)
        print(*res)


if __name__ == "__main__":
    main()
