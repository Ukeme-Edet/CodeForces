from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        x = input()
        y = input()
        i = 0
        while len(x) <= 25 and y not in x:
            x += x
            i += 1
        if y in x:
            print(i)
        else:
            print(-1)


if __name__ == "__main__":
    main()
