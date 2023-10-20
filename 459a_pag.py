from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if abs(x1 - x2) != abs(y1 - y2) and x1 != x2 and y1 != y2:
        print(-1)
    elif x1 == x2:
        print(f"{x1 + abs(y1 - y2)} {y1} {x2 + abs(y1 - y2)} {y2}")
    elif y1 == y2:
        print(f"{x1} {y1 + abs(x1 - x2)} {x2} {y2 + abs(x1 - x2)}")
    else:
        print(f"{x1} {y2} {x2} {y1}")


if __name__ == "__main__":
    main()
