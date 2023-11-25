from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(_) for _ in input().split()]
    a = sorted([int(_) for _ in input().split()])
    print(n - bisect_left(a, max(1, a[n - k])))


if __name__ == "__main__":
    main()
