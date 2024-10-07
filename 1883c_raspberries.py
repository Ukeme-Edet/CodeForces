"""
@file: 1883c_raspberries.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Raspberries(https://codeforces.com/problemset/problem/1883/C)
@version: 1.0
@date: 2024-10-07

@copyright: Copyright (c) 2024
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(_) for _ in input().split()]
        a = [int(_) for _ in input().split()]
        md = defaultdict(int)
        for ai in a:
            md[ai % k] += 1
        if md[0] or (k == 4 and md[2] > 1):
            print(0)
        elif (
            k == 2
            or (k == 3 and md[2])
            or (k == 4 and (md[3] or (md[2] and md[1])))
            or (k == 5 and md[4])
        ):
            print(1)
        elif k == 3 or (k == 4 and (md[1] > 1 or md[2])) or (k == 5 and md[3]):
            print(2)
        elif k == 4 or (k == 5 and md[2]):
            print(3)
        else:
            print(4)


if __name__ == "__main__":
    main()
