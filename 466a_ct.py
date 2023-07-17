from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m, a, b = map(int, input().split())
    if b / m >= a:
        print(n * a)
    else:
        if (n % m) * a > b:
            print((n // m) * b + b)
        else:
            print(((n // m) * b) + ((n % m) * a))


if __name__ == "__main__":
    main()
