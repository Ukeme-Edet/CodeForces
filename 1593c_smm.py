from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(_) for _ in input().split()]
        x = sorted([int(_) for _ in input().split()], reverse=True)
        cp = s = 0
        for i in x:
            if n - cp <= n - i:
                break
            s += 1
            cp += n - i
        print(s)


if __name__ == "__main__":
    main()
