from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        input()
        a = [[int(x), i] for i, x in enumerate(input().split())]
        b = [int(x) for x in input().split()]
        a.sort(key=lambda x: x[0])
        b.sort()
        a = [[b[i], x[1]] for i, x in enumerate(a)]
        a.sort(key=lambda x: x[1])
        print(" ".join([str(x[0]) for x in a]))


if __name__ == "__main__":
    main()
