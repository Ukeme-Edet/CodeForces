from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = sorted([int(x) for x in input().split()], reverse=True)
    if a.count(0) == 0:
        print(-1)
        return
    i = 8
    while i < n:
        if a[i] == 0:
            break
        i += 9
    print(int("5" * (i - 8) + "0" * a.count(0)))


if __name__ == "__main__":
    main()
