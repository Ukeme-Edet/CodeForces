"""
@file: 2025c_ng.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem New Game(https://codeforces.com/contest/2025/problem/C)
@version: 1.0
@date: 2024-10-14

@copyright: Copyright (c) 2024
"""

from collections import Counter, defaultdict
from queue import Queue
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        _, k = [int(x) for x in input().split()]
        a = defaultdict(int, Counter([int(x) for x in input().split()]))
        res, cs = 0, 0
        key_queue = Queue(k)
        for key in sorted(a.keys()):
            if not key_queue.empty() and key - key_queue.queue[-1] > 1:
                cs = 0
                key_queue = Queue(k)
            cs += a[key]
            if key_queue.qsize() == k:
                cs -= a[key_queue.get()]
            key_queue.put(key)
            res = max(res, cs)
        print(res)


if __name__ == "__main__":
    main()
