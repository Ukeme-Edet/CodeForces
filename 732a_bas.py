from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    k, r = [int(x) for x in input().split()]
    k %= 10
    a, i = k, 1
    while k % 10 != r and k % 10 != 0:
        k += a
        i += 1
    print(i)


if __name__ == "__main__":
    main()
