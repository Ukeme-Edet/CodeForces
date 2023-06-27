from sys import stdin, stdout
from math import ceil


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = map(int, input().split())
    if k <= ceil(n / 2):
        print(2 * k - 1)
    else:
        print(2 * (k - ceil(n / 2)))


if __name__ == "__main__":
    main()
