from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(x) for x in input().split()]
    k, i = 240 - k, 0
    while k and i < n:
        if k >= (i + 1) * 5:
            i += 1
            k -= i * 5
        else:
            break
    print(i)


if __name__ == "__main__":
    main()
