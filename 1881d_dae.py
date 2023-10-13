from math import sqrt
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
        prod = 1
        for i in range(n):
            prod *= a[i]
        l, r = 1, 2000000
        while l <= r:
            m = (l + r) // 2
            pa = m ** n
            if pa == prod:
                print("YES")
                break
            elif pa < prod:
                l = m + 1
            else:
                r = m - 1
        else:
            print("NO")


if __name__ == "__main__":
    main()
