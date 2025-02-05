"""
@file: 1411b_fn.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Fair Numbers(https://codeforces.com/problemset/problem/1411/B)
@version: 1.0
@date: 2025-02-05

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
        while True:
            if all(int(x) == 0 or not n % int(x) for x in str(n)):
                print(n)
                break
            n += 1


if __name__ == "__main__":
    main()
