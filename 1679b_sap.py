"""
@file: 1679b_sap.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Stone Age Problem(https://codeforces.com/problemset/problem/1679/B)
@version: 1.0
@date: 2024-12-13

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    init = [1] * n
    lc, ev = -1, 1
    s = sum(a)
    for _ in range(q):
        line = [int(x) for x in input().split()]
        if line[0] == 2:
            lc = line[1]
            s = lc * n
            ev += 1
        else:
            if init[line[1] - 1] == ev:
                s -= a[line[1] - 1]
            else:
                init[line[1] - 1] = ev
                s -= lc
            s += line[2]
            a[line[1] - 1] = line[2]
        print(s)


if __name__ == "__main__":
    main()
