"""
@file: 1582c_gckas.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Grandma Capa Knits a Scarf(https://codeforces.com/problemset/problem/1582/C)
@version: 1.0
@date: 2025-01-06

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        res = float("inf")
        for c in "abcdefghijklmnopqrstuvwxyz":
            l, r = 0, n - 1
            tres = 0
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                elif s[l] == c:
                    l += 1
                    tres += 1
                elif s[r] == c:
                    r -= 1
                    tres += 1
                else:
                    tres = float("inf")
                    break
            res = min(res, tres)
        print(res if res != float("inf") else -1)


if __name__ == "__main__":
    main()
