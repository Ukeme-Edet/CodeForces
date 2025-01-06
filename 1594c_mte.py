"""
@file: 1594c_mte.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Make Them Equal(https://codeforces.com/problemset/problem/1594/C)
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
        n, c = input().split()
        n = int(n)
        s = input()
        if all(c == x for x in s):
            print("0")
        elif c in s[n // 2 :]:
            print(f"1\n{s[n//2:].find(c) + 1 + n//2}")
        else:
            print(f"2\n{n//2+1} {n//2 + 2}")


if __name__ == "__main__":
    main()
