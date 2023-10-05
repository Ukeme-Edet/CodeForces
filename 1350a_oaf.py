from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        if n % 2 == 0:
            print(n + 2 * k)
        else:
            for i in range(3, n + 1, 2):
                if n % i == 0:
                    print(n + i + 2 * (k - 1))
                    break


if __name__ == "__main__":
    main()
