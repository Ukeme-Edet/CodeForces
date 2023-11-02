from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    mi = 0
    for i in range(n - 1):
        s = a[i] + a[i + 1]
        if s < k:
            mi += k - s
            a[i + 1] += k - s
    print(mi)
    print(" ".join([str(x) for x in a]))


if __name__ == "__main__":
    main()
