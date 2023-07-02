from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    f.sort()
    min_diff = f[n-1] - f[0]
    for i in range(m-n+1):
        min_diff = min(min_diff, f[i+n-1] - f[i])
    print(min_diff)


if __name__ == "__main__":
    main()
