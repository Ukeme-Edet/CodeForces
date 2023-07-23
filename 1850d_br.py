from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = sorted([int(x) for x in input().split()])
        if n == 1:
            print(0)
            continue
        subs, l = [], 1
        for i in range(1, n):
            if a[i] - a[i - 1] > k:
                subs.append(l)
                l = 1
            else:
                l += 1
        if i == n - 1:
            subs.append(l)
        print(n - max(subs))


if __name__ == "__main__":
    main()
