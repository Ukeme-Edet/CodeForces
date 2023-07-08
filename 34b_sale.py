from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    a = [x for x in a if x < 0]
    if len(a) <= m:
        print(abs(sum(a)))
    else:
        print(abs(sum(a[:m])))


if __name__ == "__main__":
    main()
