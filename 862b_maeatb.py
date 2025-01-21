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
    cm = {True: 0, False: 0}
    q = deque([(1, True)])
    visited = [False] * (n + 1)
    visited[1] = True
    while q:
        u, c = q.popleft()
        cm[c] += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append((v, not c))
    print(cm[True] * cm[False] - (n - 1))


if __name__ == "__main__":
    main()
