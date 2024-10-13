"""
@file: 2022b_ks.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Kar Salesman(https://codeforces.com/problemset/problem/2022/B)
@version: 1.0
@date: 2024-10-13

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, x = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        print(max(max(a), (sum(a) + x - 1) // x))


if __name__ == "__main__":
    main()
