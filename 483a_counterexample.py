from sys import stdin, stdout
from math import gcd


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    l, r = [int(_) for _ in input().split()]
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            for k in range(j + 1, r + 1):
                if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(i, k) != 1:
                    print(f"{i} {j} {k}")
                    return
    print(-1)


if __name__ == "__main__":
    main()
