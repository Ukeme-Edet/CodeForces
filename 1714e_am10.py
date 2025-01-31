"""
@file: 1714e_am10.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Add Modulo 10(https://codeforces.com/problemset/problem/1714/E)
@version: 1.0
@date: 2025-01-30

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
        a = [int(x) for x in input().split()]
        if any(not x % 10 or x % 10 == 5 for x in a):
            for i in range(n):
                if a[i] % 10 == 5:
                    a[i] += 5
            print("YES" if all(x == a[0] for x in a) else "NO")
        else:
            for i in range(n):
                while a[i] % 10 != 8:
                    a[i] += a[i] % 10
            print("YES" if all(not abs(x - a[0]) % 20 for x in a) else "NO")


if __name__ == "__main__":
    main()
