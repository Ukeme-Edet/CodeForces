from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(" ".join([str(_) for _ in sorted([int(_)
              for _ in input().split()], reverse=True)]))


if __name__ == "__main__":
    main()
