from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, x = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        mi = ma = a[0]
        s = 0
        for i in a:
            mi, ma = min(mi, i), max(ma, i)
            if ma - mi > x * 2:
                s += 1
                mi = ma = i
        print(s)


if __name__ == "__main__":
    main()
