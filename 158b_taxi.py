from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    groups = [int(x) for x in input().split()]
    groups.sort(reverse=True)
    taxis = 0
    i = 0
    j = n - 1
    while i <= j:
        if groups[i] == 4:
            taxis += 1
            i += 1
        elif groups[i] + groups[j] <= 4 and i != j:
            groups[i] += groups[j]
            j -= 1
        else:
            taxis += 1
            i += 1
    print(taxis)


if __name__ == "__main__":
    main()
