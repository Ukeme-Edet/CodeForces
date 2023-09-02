from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = [int(x) for x in input().split()]
        a = [b[0]]
        for i in range(1, n):
            a.append(b[i])
            if b[i] < b[i - 1]:
                a.append(b[i])
        print(len(a))
        print(" ".join([str(x) for x in a]))


if __name__ == "__main__":
    main()
