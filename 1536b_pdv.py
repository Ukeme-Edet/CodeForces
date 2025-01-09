"""
@file: 1536b_pdv.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Prinzessin der Verurteilung(https://codeforces.com/problemset/problem/1536/B)
@version: 1.0
@date: 2025-01-09

@copyright: Copyright (c) 2025
"""

from collections import deque
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        _ = int(input())
        s = input()
        qu = deque([""])
        while qu:
            x = qu.popleft()
            if x not in s:
                print(x)
                break
            for c in "abcdefghijklmnopqrstuvwxyz":
                qu.append(x + c)


if __name__ == "__main__":
    main()
