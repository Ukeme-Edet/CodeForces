from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    days = [int(x) for x in input().split()]
    ppw = sum(days)
    while ppw < n:
        n -= ppw
    i = 0
    while n > 0:
        n -= days[i]
        i += 1
    print(i)


if __name__ == "__main__":
    main()
