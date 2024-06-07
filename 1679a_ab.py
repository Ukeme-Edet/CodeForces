from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 4 or n % 2:
            print(-1)
            continue
        nf, ns = (n % 6) // 4, n // 6
        while nf * 4 + ns * 6 != n and ns > -1:
            ns -= 1
            nf = (n - ns * 6) // 4
        mib = ns + nf
        nf, ns = n // 4, 0
        while nf * 4 + ns * 6 != n and nf > -1:
            nf -= 1
            ns = (n - nf * 4) // 6
        mab = ns + nf
        print(f"{mib} {mab}")


if __name__ == "__main__":
    main()
