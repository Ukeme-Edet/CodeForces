import math
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        l, r, x = map(int, input().split())
        ans = r // x + r % x
        m = r // x * x - 1
        if m >= l:
            ans = max(ans, m // x + m % x)
        print(ans)


if __name__ == "__main__":
    main()
