from math import inf
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
        smallest_odd = inf
        for i in range(n):
            if a[i] % 2 != 0:
                if a[i] < smallest_odd:
                    smallest_odd = a[i]
        printed = False
        if smallest_odd == inf:
            print("YES")
            printed = True
            continue
        for i in range(n):
            if a[i] % 2 == 0 and a[i] <= smallest_odd:
                print("NO")
                printed = True
                break
        if not printed:
            print("YES")


if __name__ == "__main__":
    main()
