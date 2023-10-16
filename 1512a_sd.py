from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([[int(x), i] for i, x in enumerate(input().split())])
        print(a[0][1] + 1 if a[0][0] != a[1][0] else a[-1][1] + 1)


if __name__ == "__main__":
    main()
