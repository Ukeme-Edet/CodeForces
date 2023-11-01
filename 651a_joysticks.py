from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a1, a2 = [int(x) for x in input().split()]
    time = 0
    while a1 > 0 and a2 > 0:
        if a1 < a2:
            a1 += 1
            a2 -= 2
        else:
            a2 += 1
            a1 -= 2
        if a1 >= 0 and a2 >= 0:
            time += 1
    print(time)


if __name__ == "__main__":
    main()
