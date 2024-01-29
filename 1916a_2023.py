from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(_) for _ in input().split()]
        b = [int(_) for _ in input().split()]
        prod = 1
        for i in range(n):
            prod *= b[i]
        if 2023 % prod:
            print("NO")
            continue
        print("YES")
        print(f"{2023 // prod} " + "1 " * (k - 1))


if __name__ == "__main__":
    main()
