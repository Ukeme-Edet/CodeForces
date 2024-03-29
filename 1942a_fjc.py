from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        if n == k:
            print("1 " * k)
            continue
        if k != 1:
            print("-1")
            continue
        res = [0] * n
        for i in range(n):
            res[i] = i + 1
        print(" ".join([str(x) for x in res]))


if __name__ == "__main__":
    main()
