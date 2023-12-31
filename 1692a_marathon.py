from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        lol = [int(x) for x in input().split()]
        c = 0
        for i in lol:
            if i > lol[0]:
                c += 1
        print(c)


if __name__ == "__main__":
    main()
