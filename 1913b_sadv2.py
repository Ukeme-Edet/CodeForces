"""
@file: 1913b_sadv2.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Swap and Delete(https://codeforces.com/problemset/problem/1913/B)
@version: 1.0
@date: 2025-01-01

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        zc, oc, i = s.count("0"), s.count("1"), 0
        while i < len(s):
            if (s[i] == "0" and oc == 0) or (s[i] == "1" and zc == 0):
                break
            if s[i] == "0":
                oc -= 1
            else:
                zc -= 1
            i += 1
        print(len(s) - i)


if __name__ == "__main__":
    main()
