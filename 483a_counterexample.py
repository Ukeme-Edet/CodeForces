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
            if gcd(i, j) == 1:
                for k in range(j + 1, r + 1):
                    gki, gkj = gcd(k, i), gcd(k, j)
                    if (gkj == 1 and gki != 1) or (gkj != 1 and gki == 1):
                        print(" ".join(sorted([str(_) for _ in [i, j, k]])))
                        return
    print(-1)


if __name__ == "__main__":
    main()
