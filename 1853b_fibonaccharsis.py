from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if k > n:
            print(0)
            continue
        a, fibn = fibo(k)
        f2 = 0
        if fibn > n:
            print(0)
        else:


def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return a, b


if __name__ == "__main__":
    main()
