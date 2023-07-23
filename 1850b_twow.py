from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        max_i, max_q = 0, 0
        for i in range(n):
            a, b = [int(x) for x in input().split()]
            if a < 11 and b > max_q:
                max_i, max_q = i + 1, b
        print(max_i)


if __name__ == "__main__":
    main()
