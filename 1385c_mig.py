from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        dec, i = False, n - 1
        while i > 0:
            if a[i] < a[i - 1] and dec:
                break
            if a[i] > a[i - 1]:
                dec = True
            i -= 1
        print(i)


if __name__ == "__main__":
    main()
