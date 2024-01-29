from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(_) for _ in input().split()]
        b = [int(_) for _ in input().split()]
        fi = {1: n if 1 not in a else a.index(
            1), -1: n if -1 not in a else a.index(-1)}
        for i in range(n - 1, -1, -1):
            if a[i] < b[i] and fi[1] >= i:
                print("NO")
                break
            elif a[i] > b[i] and fi[-1] >= i:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
