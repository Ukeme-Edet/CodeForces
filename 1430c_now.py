from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("2")
        a, b = n, n - 1
        while b > 0:
            print(f"{a} {b}")
            a = (a + b + 1) // 2
            b -= 1


if __name__ == "__main__":
    main()
