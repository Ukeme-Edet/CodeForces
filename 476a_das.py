from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    if m > n:
        print(-1)
    else:
        if m >= ((n // 2) + (n % 2)):
            print(m)
        elif ((n // 2) + (n % 2)) % m == 0 and m > 1:
            print(((n // 2) + (n % 2)))
        else:
            print((n // 2) + (m - (n // 2) % m))


if __name__ == "__main__":
    main()
