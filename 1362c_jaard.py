"""
@file: 1362c_jaard.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Johnny and Another Rating Drop(https://codeforces.com/problemset/problem/1362/C)
@version: 1.0
@date: 2025-02-09

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
        res = 0
        while n:
            res += n
            n >>= 1
        print(res)


if __name__ == "__main__":
    main()
