from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    if n == 0:
        print(1)
    else:
        cases = [8, 4, 2, 6]
        print(cases[(n - 1) % 4])


if __name__ == "__main__":
    main()
