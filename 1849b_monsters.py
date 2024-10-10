"""
@file: 1849b_monsters.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Monsters(https://codeforces.com/problemset/problem/1849/B)
@version: 1.0
@date: 2024-10-10

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
        _, k = [int(x) for x in input().split()]
        a = [(int(x) % k, i) for i, x in enumerate(input().split())]
        a.sort(key=lambda x: (-float("inf") if x[0] == 0 else -x[0], x[1]))
        print(" ".join(str(x[1] + 1) for x in a))


if __name__ == "__main__":
    main()
