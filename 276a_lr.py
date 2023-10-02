from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(x) for x in input().split()]
    res = float("-inf")
    for _ in range(n):
        f, t = [int(x) for x in input().split()]
        if t > k:
            res = max(res, f - (t - k))
        else:
            res = max(res, f)
    print(res)


if __name__ == "__main__":
    main()
