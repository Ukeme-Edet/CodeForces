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
        a.sort()
        for i in range(0, n - 1 - (n % 2), 2):
            if a[i] <= 0 and a[i + 1] <= 0:
                a[i], a[i + 1] = -a[i], -a[i + 1]
            elif a[i] <= 0 and abs(a[i]) > abs(a[i + 1]) or a[i + 1] <= 0 and abs(a[i]) < abs(a[i + 1]):
                a[i], a[i + 1] = -a[i], -a[i + 1]
        print(sum(a))


if __name__ == "__main__":
    main()
