from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m, k = map(int, input().split())
    armies = []
    p_friends = 0
    for _ in range(m):
        army = int(input())
        armies.append(army)
    f_army = int(input())
    for army in armies:
        same = 0
        for i in range(n):
            if (f_army >> i) & 1 == (army >> i) & 1:
                same += 1
        if n - same <= k:
            p_friends += 1
    print(p_friends)


if __name__ == "__main__":
    main()
