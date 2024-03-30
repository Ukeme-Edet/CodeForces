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
        if len(a) == 1:
            print(0)
            continue
        md = -float("inf")
        for i in range(n - 1):
            md = max(md, a[i] - a[i + 1])
        md = max(md, a[n - 1] - min(a[:n - 1]), max(a[1:]) - a[0])
        print(md)


if __name__ == "__main__":
    main()
