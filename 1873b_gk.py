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
        mina, prod = 0, 1
        for i in range(1, n):
            if a[i] <= a[mina]:
                mina = i
        a[mina] += 1
        for i in range(n):
            prod *= a[i]
        print(prod)


if __name__ == "__main__":
    main()
