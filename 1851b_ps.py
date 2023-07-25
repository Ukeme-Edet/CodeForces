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
        b = [x for x in a]
        b.sort()
        for ai in range(n):
            if a[ai] % 2 != b[ai] % 2:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
