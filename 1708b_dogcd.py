"""
@file: 1708b_dogcd.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Difference of GCDs(https://codeforces.com/problemset/problem/1708/B)
@version: 1.0
@date: 2025-01-16

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, l, r = [int(x) for x in input().split()]
        res = [0] * n
        for i in range(1, n + 1):
            if i - (l % i) <= r - l or not l % i:
                res[i - 1] = l + i - (l % i) if l % i else l
            else:
                print("NO")
                break
        else:
            print("YES")
            print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
