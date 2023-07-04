from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    if n > 0:
        print(n)
        return
    n = str(n)
    print(int(n[:-1]) if n[-1] > n[-2] else int(n[:-2] + n[-1]))


if __name__ == "__main__":
    main()
