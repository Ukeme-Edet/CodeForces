"""
@file: 1904a_forked.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Forked!(https://codeforces.com/problemset/problem/1904/A)
@version: 1.0
@date: 2025-02-06

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        a, b = [int(x) for x in input().split()]
        xk, yk = [int(x) for x in input().split()]
        xq, yq = [int(x) for x in input().split()]
        apk, apq = set(), set()
        for dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            apk.add((xk + dir[0] * a, yk + dir[1] * b))
            apk.add((xk + dir[0] * b, yk + dir[1] * a))
            apq.add((xq + dir[0] * a, yq + dir[1] * b))
            apq.add((xq + dir[0] * b, yq + dir[1] * a))
        print(len(apk & apq))


if __name__ == "__main__":
    main()
