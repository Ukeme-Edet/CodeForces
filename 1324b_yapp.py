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
        sequence = {a[0]: False, a[1]: False}
        for i in range(2, n):
            sequence[a[i - 2]] = True
            if a[i] in sequence and sequence[a[i]]:
                print("YES")
                break
            else:
                sequence[a[i]] = False
        else:
            print("NO")


if __name__ == "__main__":
    main()
