"""
@file: 1919c_gi.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Grouping Increases(https://codeforces.com/contest/1919/problem/C)
@version: 1.0
@date: 2024-10-15

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
        a = [int(x) for x in input().split()]
        res, s1, s2 = 0, float("inf"), float("inf")
        for ai in a:
            if ai <= s1 and ai <= s2:
                if s1 > s2:
                    s2 = ai
                else:
                    s1 = ai
            elif ai > s1 and ai <= s2:
                s2 = ai
            elif ai > s2 and ai <= s1:
                s1 = ai
            else:
                res += 1
                if s1 > s2:
                    s2 = ai
                else:
                    s1 = ai
        print(res)


if __name__ == "__main__":
    main()
