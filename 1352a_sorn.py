from sys import stdin


def input():
    return stdin.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        n = input()
        nz = sum([1 if int(x) != 0 else 0 for x in n])
        l, n = len(n), int(n)
        print(nz)
        d = 10 ** (l - 1)
        while n:
            if n // d:
                print((n // d) * d, end=" ")
            n %= d
            d //= 10
        print("")


if __name__ == "__main__":
    main()
