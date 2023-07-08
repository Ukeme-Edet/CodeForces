from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cut_ropes = 0
        for i in range(n):
            a, b = map(int, input().split())
            if b < a:
                cut_ropes += 1
        print(cut_ropes)


if __name__ == "__main__":
    main()
