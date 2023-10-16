from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        ms = [int(x) for x in input().split()]
        if sum(ms) % 9 == 0 and min(ms) >= sum(ms) // 9:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
