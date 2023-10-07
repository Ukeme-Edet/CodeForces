from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    for i in range(n * 2 + 1):
        s = ' '.join([str(x) for x in range(min(n, i) + 1)])
        if i > n:
            s = s[:-(i - n) * 2].strip()
        print(
            f"{'  ' * (abs(n - i)) + s + ''.join(str(x) for x in reversed(s[:-1]))}".rstrip())


if __name__ == "__main__":
    main()
