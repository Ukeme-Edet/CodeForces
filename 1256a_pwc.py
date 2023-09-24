from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    q = int(input())
    for _ in range(q):
        a, b, n, s = [int(x) for x in input().split()]
        t = s // n
        print("YES" if (s % n == 0 or n * t + b >= s)
              and (t <= a or (a * n) + b >= s) else "NO")


if __name__ == "__main__":
    main()
