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
        for i in range(n - 1, -1, -1):
            if n >= a[i]:
                break
            n -= 1
        print(n + 1)


if __name__ == "__main__":
    main()
