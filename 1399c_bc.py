from math import floor
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        w = sorted([int(x) for x in input().split()])
        if n == 1:
            print(0)
            continue
        maxtc = 0
        maxtw, mintw = w[-1] + w[-2], w[0] + w[1]
        for weight in range(mintw, maxtw + 1):
            l, r = 0, n - 1
            tc = 0
            while l < r:
                if w[l] + w[r] == weight:
                    tc += 1
                    l += 1
                    r -= 1
                elif w[l] + w[r] < weight:
                    l += 1
                else:
                    r -= 1
            maxtc = max(maxtc, tc)
        print(maxtc)


if __name__ == "__main__":
    main()
