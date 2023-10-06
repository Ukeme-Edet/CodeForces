from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    energy, cash = 0, h[0]
    for i in range(1, n):
        energy += h[i - 1] - h[i]
        if energy < 0:
            cash += abs(energy)
            energy = 0
    print(cash)


if __name__ == "__main__":
    main()
