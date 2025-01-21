"""
@file: 862b_maeatb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Mahmoud and Ehab and the bipartiteness(https://codeforces.com/problemset/problem/862/B)
@version: 1.0
@date: 2025-01-21

@copyright: Copyright (c) 2025
"""

from collections import deque
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (n + 1)
    l = 0
    ls, rs = 0, 0
    queue = deque([1])
    while queue:
        next_queue = deque()
        while queue:
            u = queue.popleft()
            visited[u] = True
            ls += 1 - l
            rs += l
            next_queue.extend(v for v in adj[u] if not visited[v])
        queue = next_queue
        l = 1 - l
    print(ls * rs - (n - 1))


if __name__ == "__main__":
    main()
