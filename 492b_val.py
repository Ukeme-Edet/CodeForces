from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, l = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    max_d = 0
    for i in range(1, len(a)):
        max_d = max(a[i] - a[i - 1], max_d)
    print(max([a[0], max_d / 2, l - a[-1]]))


if __name__ == "__main__":
    main()
