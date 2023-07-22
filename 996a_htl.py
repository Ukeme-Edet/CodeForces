from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, ns, i = int(input()), 0, 0
    ds = [100, 20, 10, 5, 1]
    while n % ds[i] != 0:
        ns += n // ds[i]
        n %= ds[i]
        i += 1
    print(ns + (n // ds[i]))


if __name__ == "__main__":
    main()
