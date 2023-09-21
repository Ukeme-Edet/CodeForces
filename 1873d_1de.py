from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        s, i, m = input(), 0, 0
        while i < n:
            if s[i] == "B":
                m += 1
                i += k
            else:
                i += 1
        print(m)


if __name__ == "__main__":
    main()
