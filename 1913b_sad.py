"""
@file: 1913b_sad.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Swap and Delete(https://codeforces.com/problemset/problem/1913/B)
@version: 1.0
@date: 2024-10-06

@copyright: Copyright (c) 2024
"""

from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        sm = defaultdict(int, Counter(s))
        im = {"1": "0", "0": "1"}
        for i in range(len(s)):
            if not sm[im[s[i]]]:
                print(len(s) - i)
                break
            sm[im[s[i]]] -= 1
        else:
            print(0)


if __name__ == "__main__":
    main()
