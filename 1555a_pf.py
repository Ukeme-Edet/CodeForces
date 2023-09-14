from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ns = ceil(n / 6)
        if n < 6:
            print(15)
            continue
        result = ns * 15
        if (ns - 2) * 6 + 8 >= n:
            result = min((ns - 2) * 15 + 20, result)
        if (ns - 2) * 6 + 10 >= n:
            result = min((ns - 2) * 15 + 25, result)
        print(result)


if __name__ == "__main__":
    main()
