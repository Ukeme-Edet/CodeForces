"""
@file: 1485a_aad.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Add and Divide(https://codeforces.com/contest/1485/problem/A)
@version: 1.0
@date: 2024-09-02

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
        a, b = [int(_) for _ in input().split()]
        res = 0
        ans = float("inf")
        if b == 1:
            res += 1
            b = 2
        while True:
            ac, c = a, 0
            while ac > 0:
                ac //= b
                c += 1
            ans = min(ans, res + c)
            res += 1
            b += 1
            if res > ans:
                break
        print(ans)


if __name__ == "__main__":
    main()
