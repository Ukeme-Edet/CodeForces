from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _ = int(input())
    pairings = [[int(x), i+1] for i, x in enumerate(input().split())]
    pairings.sort(key=lambda x: x[0])
    print(" ".join([str(x[1]) for x in pairings]))


if __name__ == "__main__":
    main()
