"""
@file: 1726a_maa2.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Mainak and Array(https://codeforces.com/problemset/problem/1726/A)
@version: 1.0
@date: 2025-02-13

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
        print(
            max(
                [
                    max(a[1:], default=a[0]) - a[0],
                    a[-1] - min(a[:-1], default=a[-1]),
                    max([a[i] - a[i + 1] for i in range(n - 1)], default=0),
                ]
            )
        )


if __name__ == "__main__":
    main()
