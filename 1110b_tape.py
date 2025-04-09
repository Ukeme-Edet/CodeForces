"""
@file: 1110b_tape.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Tape(https://codeforces.com/problemset/problem/1110/B)
@version: 1.0
@date: 2025-04-03

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    m, n, k = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    diff = [b[i] - b[i - 1] - 1 for i in range(1, m)]
    diff.sort(reverse=True)
    od = b[-1] - b[0] + 1
    print(od - sum(diff[: k - 1]))


if __name__ == "__main__":
    main()
