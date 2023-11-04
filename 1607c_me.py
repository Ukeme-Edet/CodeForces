from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([int(x) for x in input().split()])
        ans = a[0]
        for i in range(1, n):
            ans = max(ans, a[i] - a[i - 1])
        print(ans)


if __name__ == "__main__":
    main()
