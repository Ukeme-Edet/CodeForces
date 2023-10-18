from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        if n % 2:
            if k % 2:
                if k <= n:
                    print("YES\n" + ("1 " * (k - 1) + str(n - k + 1)).strip())
                else:
                    print("NO")
            else:
                print("NO")
        else:
            if k % 2:
                if k * 2 <= n:
                    print("YES\n" + ("2 " * (k - 1) +
                          str(n - (k * 2) + 2)).strip())
                else:
                    print("NO")
            else:
                if k <= n:
                    print("YES\n" + ("1 " * (k - 1) + str(n - k + 1)).strip())
                else:
                    print("NO")


if __name__ == "__main__":
    main()
