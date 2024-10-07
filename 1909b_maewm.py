"""
@file: 1909b_maewm.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Make Almost Equal With Mod(https://codeforces.com/problemset/problem/1909/B)
@version: 1.0
@date: 2024-10-07

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
        n = int(input())
        a = [int(_) for _ in input().split()]
        d = 2
        while len(set([ai % d for ai in a])) != 2:
            d *= 2
        print(d)


if __name__ == "__main__":
    main()
