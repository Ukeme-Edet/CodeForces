from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    if k == 0:
        if a[0] == 1:
            print(-1)
        else:
            print(1)
    elif k == n:
        print(a[-1])
    else:
        if a[k - 1] == a[k]:
            print(-1)
        else:
            print(a[k - 1])


if __name__ == "__main__":
    main()
