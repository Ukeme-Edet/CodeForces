from math import log
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        lg = 0
        for ai in a:
            lg += log(ai, 10)
        lg /= n
        ans = 10 ** lg
        if abs(ans - round(ans)) < 1e-6:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
