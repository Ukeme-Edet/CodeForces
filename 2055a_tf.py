"""
@file: 2055a_tf.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Two Frogs(https://codeforces.com/contest/2055/problem/A)
@version: 1.0
@date: 2025-01-12

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, a, b = [int(x) for x in input().split()]
        print("YES" if (abs(a - b) - 1) % 2 else "NO")


if __name__ == "__main__":
    main()
