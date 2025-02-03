"""
@file: 2059a_mata.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Milya and Two Arrays(https://codeforces.com/contest/2059/problem/A)
@version: 1.0
@date: 2025-02-02

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
        a = sorted(int(x) for x in input().split())
        b = sorted(int(x) for x in input().split())
        t = set()
        i = j = la = 0
        while i < n:
            j = la
            while j < n:
                if a[i] + b[j] not in t:
                    t.add(a[i] + b[j])
                    la = j + 1
                    break
                j += 1
            i += 1
            j = la + 1
        print("YES" if len(t) > 2 else "NO")


if __name__ == "__main__":
    main()
