from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, c, d = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        ia = defaultdict(int, Counter(a))
        pg = [0] * (n * n)
        pg[0] = min(a)
        for i in range(n):
            for j in range(1, n):
                pg[(i * n) + j] = pg[(i * n) + j - 1] + d
            if i < n - 1:
                pg[(i + 1) * n] = pg[(i * n)] + c
        ipg = defaultdict(int, Counter(pg))
        for key in ipg.keys():
            if ia[key] != ipg[key]:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
