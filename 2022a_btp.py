"""
@file: 2022a_.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Bus to Pénjamo(https://codeforces.com/problemset/problem/2022/A)
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
        _, r = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        res, op = 0, 0
        for ai in a:
            res += ai // 2
            op += ai % 2
        res *= 2
        er = res // 2
        res += op
        while op > r - er:
            res -= 2
            op -= 1
        print(res)


if __name__ == "__main__":
    main()
