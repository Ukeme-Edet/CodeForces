from math import lcm
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    if m % n != 0:
        print(-1)
        return
    d, i = m // n, 0
    while d != 1:
        if d % 2 == 0:
            d //= 2
        elif d % 3 == 0:
            d //= 3
        else:
            break
        i += 1
    print(i if d == 1 else -1)


if __name__ == "__main__":
    main()
