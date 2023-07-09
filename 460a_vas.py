from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = map(int, input().split())
    r = n % m
    total = 0
    total = (n // m) * m
    q = n // m
    while q + r >= m:
        total += ((q + r) // m) * m
        temp = r
        r = (q + r) % m
        q = (((q + temp) // m) * m) // m
    total += q + r
    print(total)


if __name__ == "__main__":
    main()
