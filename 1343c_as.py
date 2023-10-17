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
        i = 0
        ans, cmax = [], a[0]
        while i < n:
            i += 1
            while i < n and abs(a[i]) // a[i] == abs(a[i - 1]) // a[i - 1]:
                cmax = max(cmax, a[i])
                i += 1
            ans.append(cmax)
            if i < n:
                cmax = a[i]
        print(sum(ans))


if __name__ == "__main__":
    main()
