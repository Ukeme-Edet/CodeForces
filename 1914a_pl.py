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
        log = defaultdict(int, Counter([s for s in input()]))
        solved = 0
        for k, v in log.items():
            if v >= ord(k) - ord("A") + 1:
                solved += 1
        print(solved)


if __name__ == "__main__":
    main()
