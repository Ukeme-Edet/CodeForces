from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(_) for _ in input().split()]
        print("YES" if is_square(sum(a)) else "NO")


def is_square(n):
    return int(n**0.5)**2 == n


if __name__ == "__main__":
    main()
