"""
@file: 1543a_eb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Exciting Bets(https://codeforces.com/problemset/problem/1543/A)
@version: 1.0
@date: 2025-06-29

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
        gcd = abs(a - b)
        if gcd == 0:
            print(0, 0)
            continue
        print(gcd, min(gcd - a % gcd, a % gcd))


if __name__ == "__main__":
    main()
