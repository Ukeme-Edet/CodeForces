from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    my_sum = 0
    total = sum(a)
    for i in range(n):
        my_sum += a[i]
        if my_sum > total - my_sum:
            print(i + 1)
            break


if __name__ == "__main__":
    main()
