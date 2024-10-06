"""
@file: 1917b_eforl.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Erase First or Second Letter(https://codeforces.com/problemset/problem/1917/B)
@version: 1.0
@date: 2024-10-06

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
        n = int(input())
        s = input()
        sm, res = defaultdict(bool), 0
        for i in range(len(s)):
            res += n - i if not sm[s[i]] else 0
            sm[s[i]] = 1
        print(res)


if __name__ == "__main__":
    main()
