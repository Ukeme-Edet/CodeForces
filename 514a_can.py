from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    x = [int(x) for x in input()]
    for i in range(1, len(x)):
        if x[i] > 4:
            x[i] = 9 - x[i]
    if x[0] > 4 and x[0] < 9:
        x[0] = 9 - x[0]
    ans = ''.join(str(x) for x in x)
    print(ans)


if __name__ == "__main__":
    main()
