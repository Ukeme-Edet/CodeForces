from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print("YES" if b != 1 else "NO")
        if b != 1:
            print(f"{a} {a * b} {a * (b + 1)}")


if __name__ == "__main__":
    main()
