from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    pairs = 0
    i = j = 0
    while i < n and j < m:
        if abs(a[i] - b[j]) < 2:
            pairs += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(pairs)


if __name__ == "__main__":
    main()
