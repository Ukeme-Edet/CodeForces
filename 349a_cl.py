from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    queue = [int(x) for x in input().split()]
    bills = {25: 0, 50: 0}
    for person in queue:
        if person != 100:
            bills[person] += 1
        if person > 25:
            bills[25] -= 1
        if person > 50:
            if bills[50]:
                bills[50] -= 1
            else:
                bills[25] -= 2
        if bills[25] < 0:
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
