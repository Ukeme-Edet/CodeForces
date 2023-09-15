from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    ns = [int(x) for x in input().split()]
    r = 0
    for i in range(1, n):
        if ns[i] > max(ns[:i]) or ns[i] < min(ns[:i]):
            r += 1
    print(r)


if __name__ == "__main__":
    main()
