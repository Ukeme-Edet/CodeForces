from sys import stdin, stdout


def input():
    """ Faster input parsing """
    return stdin.readline().strip()


def print(string):
    stdout.write(str(string) + "\n")


def main():
    n = int(input())
    last = input()
    count = 1
    for _ in range(n-1):
        current = input()
        if last != current:
            count += 1
        last = current
    print(count)


if __name__ == "__main__":
    main()
