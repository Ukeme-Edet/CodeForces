from bisect import bisect_left, bisect_right
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        curr = max_sum = 0
        a_sum = sum(a)
        for i in range(n):
            curr += a[i]
            if curr < 0:
                curr = 0
            max_sum = max(max_sum, curr)
        if max_sum <= 0:
            print(a_sum % (10**9 + 7))
        else:
            print((max_sum * (2**k) + a_sum - max_sum) % (10**9 + 7))


if __name__ == "__main__":
    main()
