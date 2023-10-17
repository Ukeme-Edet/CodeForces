from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, x = [int(x) for x in input().split()]
        a = [int(x) % 2 for x in input().split()]
        odds = sum(a)
        evens = n - odds
        for i in range(1, min(odds, x) + 1, 2):
            if evens >= x - i:
                print("Yes")
                break
        else:
            print("No")


if __name__ == "__main__":
    main()
