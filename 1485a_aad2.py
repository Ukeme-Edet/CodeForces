"""
@file: 1485a_aad2.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem  Add and Divide(https://codeforces.com/contest/1485/problem/A)
@version: 1.0
@date: 2025-02-04

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep="", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        a, b = [int(x) for x in input().split()]
        res = pa = float("inf")
        adc = 1 if b == 1 else 0
        b += adc
        while pa <= res:
            dc, ac = 0, a
            while ac:
                ac //= b
                dc += 1
            pa = dc + adc
            res = min(res, pa)
            b += 1
            adc += 1
        print(res)


if __name__ == "__main__":
    main()
