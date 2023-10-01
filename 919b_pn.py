from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    k, i = int(input()), 0
    res = 0
    while i < k:
        res += 1
        while sum([int(x) for x in str(res)]) != 10:
            res += 1
        i += 1
    print(res)


if __name__ == "__main__":
    main()
