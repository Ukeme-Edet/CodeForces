from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) % 3 for x in input().split()]
        target, moves = n // 3, 0
        c0, c1, c2 = a.count(0), a.count(1), a.count(2)
        while c0 != c1 or c1 != c2 or c2 != c0:
            if c0 > target:
                moves += c0 - target
                c1 += c0 - target
                c0 = target
            if c1 > target:
                moves += c1 - target
                c2 += c1 - target
                c1 = target
            if c2 > target:
                moves += c2 - target
                c0 += c2 - target
                c2 = target
        print(moves)


if __name__ == "__main__":
    main()
