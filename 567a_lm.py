from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    x = sorted([int(y) for y in input().split()])
    print(f"{abs(x[0] - x[1])} {abs(x[0] - x[-1])}")
    for i in range(1, n - 1):
        print(
            f"{min(abs(x[i] - x[i - 1]), abs(x[i] - x[i + 1]))} {max(abs(x[i] - x[0]), abs(x[i] - x[-1]))}")
    print(f"{abs(x[-1] - x[-2])} {abs(x[-1] - x[0])}")


if __name__ == "__main__":
    main()
