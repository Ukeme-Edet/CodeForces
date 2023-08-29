from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = int(input())
        spent = 0
        while s >= 10:
            spent += s - s % 10
            s = s % 10 + s // 10
        print(spent + s)


if __name__ == "__main__":
    main()
