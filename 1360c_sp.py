from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        if [x % 2 for x in a].count(0) % 2 == 0:
            print("YES")
            continue
        a.sort()
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] % 2 != a[j] % 2 and abs(a[j] - a[i]) == 1:
                    print("YES")
                    break
            else:
                continue
            break
        else:
            print("NO")


if __name__ == "__main__":
    main()
