from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    for i in range(n):
        if i % 2 == 0:
            print("#" * m)
        else:
            if (i // 2) % 2 == 0:
                print("." * (m - 1) + "#")
            else:
                print("#" + "." * (m - 1))


if __name__ == "__main__":
    main()
