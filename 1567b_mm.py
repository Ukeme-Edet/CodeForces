"""
@file: 1567b_mm.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem MEXor Mixup(https://codeforces.com/contest/1567/problem/B)
@version: 1.0
@date: 2025-02-03

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    xor = 0
    xormap = {}
    for i in range(300000):
        xor ^= i
        xormap[str(i + 1)] = xor
    for _ in range(int(input())):
        a, b = [int(x) for x in input().split()]
        cxor = xormap[str(a)]
        print(a if cxor == b else a + 1 if cxor ^ b != a else a + 2)


if __name__ == "__main__":
    main()
