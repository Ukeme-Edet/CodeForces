"""
@file: 1215b_tnop.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem The Number of Products(https://codeforces.com/problemset/problem/1215/B)
@version: 1.0
@date: 2025-04-10

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ec = oc = nnc = pres = 0
    for ai in a:
        ec += 1 - nnc % 2
        oc += nnc % 2
        nnc += ai < 0
        pres += oc if nnc % 2 else ec
    print(n * (n + 1) // 2 - pres, pres)


if __name__ == "__main__":
    main()
