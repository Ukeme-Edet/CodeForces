from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        m = 0
        n = int(input())
        for i in range(1, n//2 + 1):
            l = i * 2
            m += (i * l) * 4
        print(m)


if __name__ == "__main__":
    main()
