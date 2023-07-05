from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    d = {}
    for _ in range(n):
        t = input()
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    print(max(d, key=d.get))


if __name__ == "__main__":
    main()
