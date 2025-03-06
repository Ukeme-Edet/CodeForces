"""
@file: 1679a_avtobus.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem AvtoBus(https://codeforces.com/contest/1679/problem/A)
@version: 1.0
@date: 2025-03-06

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 3 or n % 2:
            print(-1)
            continue
        x = n // 6
        while (n - 6 * x) % 4 and x:
            x -= 1
        res1 = x + (n - 6 * x) // 4
        x = n // 4
        while (n - 4 * x) % 6 and x:
            x -= 1
        res2 = x + (n - 4 * x) // 6
        print(res1, res2)


if __name__ == "__main__":
    main()
