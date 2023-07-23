from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        min_diff = 1e9
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                print(0)
                break
            else:
                min_diff = min(min_diff, a[i + 1] - a[i])
        else:
            if min_diff == 0:
                print(1)
            else:
                print((min_diff // 2) + 1)


if __name__ == "__main__":
    main()
