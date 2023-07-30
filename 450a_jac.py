from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _, m = map(int, input().split())
    z = 0
    a = [(x, int(y)) for x, y in enumerate(input().split())]
    last = a[-1][0]
    while a:
        last = a[-1][0]
        z += m
        a = [x for x in a if x[1] > z]
    print(last + 1)


if __name__ == "__main__":
    main()
