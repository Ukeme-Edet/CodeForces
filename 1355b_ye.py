from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        e = [int(_) for _ in input().split()]
        ed = defaultdict(int, Counter(e))
        ans = 0


if __name__ == "__main__":
    main()
