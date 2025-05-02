"""
@file: 2108a_pwu.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Permutation Warm-Up(https://codeforces.com/contest/2108/problem/A)
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
    pc = [0] * 501
    for i in range(1, 501):
        pc[i] = (
            i * (i + 1) // 2
            - (i // 2) * (i // 2 + 1)
            - ((i + 1) // 2 if i % 2 else 0)
        ) + 1
    for _ in range(int(input())):
        print(pc[int(input())])


if __name__ == "__main__":
    main()
