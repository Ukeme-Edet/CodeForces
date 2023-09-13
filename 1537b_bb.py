from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m, _, _ = [int(x) for x in input().split()]
        print(f"1 1 {n} {m}")


if __name__ == "__main__":
    main()
