from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ns = set()
        for i in range(1, n):
            ns.add(s[i-1:i+1])
        print(len(ns))


if __name__ == "__main__":
    main()
