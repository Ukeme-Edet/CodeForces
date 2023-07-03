import math
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    x = int(input())
    count = 0
    while x > 0:
        c = x
        x >>= 1
        count += math.ceil(c / 2) - x
    print(count)


if __name__ == "__main__":
    main()
