from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        print("W" + "B" * (m - 1))
        for i in range(n - 1):
            print("B" * m)


if __name__ == "__main__":
    main()
