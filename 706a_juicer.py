from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, b, d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a = [x for x in a if x <= b]
    waste = count = 0
    for x in a:
        count += x
        if count > d:
            waste += 1
            count = 0
    print(waste)


if __name__ == "__main__":
    main()
