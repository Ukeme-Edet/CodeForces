from bisect import bisect_right
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        journey = [(0, 0) for _ in range(n)]
        for i in range(n):
            journey[i] = tuple(int(_) for _ in input().split())
        journeyc = [jou[0] for jou in journey]
        journeyc.sort()
        ans = 0
        for jou in journey:
            ans += n - bisect_right(journeyc, jou[0])
        print(ans)


if __name__ == "__main__":
    main()
