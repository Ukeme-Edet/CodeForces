from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    ld = defaultdict(int, Counter(l))
    ld = sorted(ld.items(), key=lambda x: x[1], reverse=True)
    print(f"{ld[0][1]} {len(ld)}")


if __name__ == "__main__":
    main()
