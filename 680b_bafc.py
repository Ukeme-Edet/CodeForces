from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, a = [int(_) for _ in input().split()]
    t = [int(_) for _ in input().split()]
    a -= 1
    d = 1
    c = 0
    while a + d < len(t) and a - d > -1:
        if t[a + d] and t[a - d]:
            c += 2
        d += 1
    c += t[a]
    if a - d > -1:
        c += sum(t[:a - d + 1])
    if a + d < len(t):
        c += sum(t[a + d:])
    print(c)


if __name__ == "__main__":
    main()
