from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        if len(set(s)) == 1:
            print(s)
        else:
            print("10" * len(s))


if __name__ == "__main__":
    main()
