from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    k, l, m, n, d = int(input()), int(input()), int(
        input()), int(input()), int(input())
    count = 0
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
