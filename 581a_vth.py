from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a, b = [int(x) for x in input().split()]
    print(f"{min(a, b)} {abs(a - b) // 2}")


if __name__ == "__main__":
    main()
