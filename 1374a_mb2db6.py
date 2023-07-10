from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        count2, count3 = 0, 0
        while n % 2 == 0:
            count2 += 1
            n //= 2
        while n % 3 == 0:
            count3 += 1
            n //= 3
        if n == 1 and count2 <= count3:
            print(2 * count3 - count2)
        else:
            print(-1)


if __name__ == "__main__":
    main()
