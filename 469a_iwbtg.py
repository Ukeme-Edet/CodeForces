from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    x = [int(a) for a in input().split()]
    y = [int(a) for a in input().split()]
    print("I become the guy." if len(
        set(x[1:] + y[1:])) == n else "Oh, my keyboard!")


if __name__ == "__main__":
    main()
