from math import gcd, sqrt
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        l, r = [int(x) for x in input().split()]
        if l % 2 == 0 or r % 2 == 0:
            if l % 2 == 0 and l > 3:
                print(f"2 {l - 2}")
                continue
            if r % 2 == 0 and r > 3:
                print(f"2 {r - 2}")
                continue
        if l != r:
            a = r // 2
            b = r - a
            if a % 2 == 1:
                a -= 1
            else:
                b -= 1
            print(f"{a} {b}" if a > 1 and b > 1 else -1)
        else:
            prims = get_primes(int(sqrt(r + 1)))
            for prime in prims:
                if r % prime == 0:
                    print(f"{prime} {r - prime}")
                    break
                if l % prime == 0:
                    print(f"{prime} {l - prime}")
                    break
            else:
                print(-1)


def get_primes(n):
    primes = [True for _ in range(n + 1)]
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]


if __name__ == "__main__":
    main()
