from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    k = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    sum = 0
    for i in range(len(a)):
        if sum >= k:
            print(i)
            break
        sum += a[i]
    else:
        if sum >= k:
            print(len(a))
        else:
            print(-1)


if __name__ == "__main__":
    main()
