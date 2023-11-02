from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    d = sorted([int(x) for x in input().split()])
    rmf = get_facs(d[-1])[:-1]
    for fac in rmf:
        if fac in d:
            d.remove(fac)
    print(f"{d[-1]} {d[-2]}")


def get_facs(n):
    facts = []
    for i in range(1, n + 1):
        if n % i == 0:
            facts.append(i)
    return facts


if __name__ == "__main__":
    main()
