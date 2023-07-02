from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    min_i, max_i = 0, 0
    for i in range(n):
        if a[i] <= a[min_i]:
            min_i = i
        elif a[i] > a[max_i]:
            max_i = i
    if min_i > max_i:
        print(max_i + n - 1 - min_i)
    else:
        print(max_i + n - 2 - min_i)


if __name__ == "__main__":
    main()
