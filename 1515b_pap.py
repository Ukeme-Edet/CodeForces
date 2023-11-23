from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("YES"if (n % 2 == 0 and is_square(n // 2))
              or (n % 4 == 0 and is_square(n // 4)) else "NO")


def is_square(n):
    return n == int(n**0.5)**2


if __name__ == "__main__":
    main()
