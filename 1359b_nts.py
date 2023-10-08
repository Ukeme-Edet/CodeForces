from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m, x, y = [int(x) for x in input().split()]
        td = {1: 0, 2: 0}
        for _ in range(n):
            s = input()
            td[1] += s.count('.')
            td[2] += s.count('..')
            td[1] -= s.count('..') * 2
        if x * 2 <= y:
            print(td[2] * x * 2 + td[1] * x)
        else:
            print(td[2] * y + td[1] * x)


if __name__ == "__main__":
    main()
