from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + a[i]
    for bi in b:
        i = bisect_left(ps, bi)
        print(f"{i} {bi - ps[i - 1]}")


if __name__ == "__main__":
    main()
