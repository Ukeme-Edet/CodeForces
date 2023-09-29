from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, x = [int(x) for x in input().split()]
        a = sorted([int(x) for x in input().split()], reverse=True)
        i, sa = 1, a[0]
        while i < n and sa / i >= x:
            sa += a[i]
            i += 1
        print(i - 1 if sa / i < x else i)


if __name__ == "__main__":
    main()
