"""
@file: 1703e_mg.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Mirror Grid(https://codeforces.com/problemset/problem/1703/E)
@version: 1.0
@date: 2024-11-22

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
        grid = [input() for _ in range(n)]
        res = 0

        def count_min_moves(i, j, steps):
            mv = {"0": 0, "1": 0}
            for _ in range(steps):
                mv[grid[i][j]] += 1
                i, j = j, n - i - 1
            return min(mv.values())

        for i in range(n // 2):
            for j in range(n // 2):
                res += count_min_moves(i, j, 4)
        if n % 2:
            for i in range(n // 2):
                res += count_min_moves(i, n // 2, 4)
        print(res)


if __name__ == "__main__":
    main()
