from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = map(int, input().split())
    a = [int(x)-1 for x in input().split()]
    time, pos = 0, 0
    for i in range(m):
        if a[i] >= pos:
            time += a[i] - pos
        else:
            time += n - pos + a[i]
        pos = a[i]
    print(time)


if __name__ == "__main__":
    main()
