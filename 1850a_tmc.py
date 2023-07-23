from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        print("YES" if sum(
            sorted([int(x) for x in input().split()], reverse=True)[0:2]) >= 10 else "NO")


if __name__ == "__main__":
    main()
