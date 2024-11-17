"""
@file: 1734c_rsm.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Removing Smallest Multiples(https://codeforces.com/contest/1734/problem/C)
@version: 1.0
@date: 2024-11-17

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
        s = input()
        deleted = [False] * n
        res = 0
        for i in range(n):
            if s[i] == "0":
                for j in range(i, n, i + 1):
                    if s[j] == "1":
                        break
                    if not deleted[j]:
                        deleted[j] = True
                        res += i + 1
        print(res)


if __name__ == "__main__":
    main()
