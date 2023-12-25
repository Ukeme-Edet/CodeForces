from math import ceil, floor, log
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x = [int(x) for x in input()]
        for i in range(len(x)):
            if x[i] > 4:
                j = i
                x = x[:i + 1] + [0] * (len(x) - i - 1)
                while j >= 0 and x[j] > 4:
                    x[j] = 0
                    if j == 0:
                        x.insert(0, 1)
                        j += 1
                    else:
                        x[j - 1] += 1
                    j -= 1
        print(int("".join([str(x) for x in x])))


if __name__ == "__main__":
    main()
