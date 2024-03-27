from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, c = input().split()
        n = int(n)
        s = input()
        ans = 0
        if s[-1] == "g":
            ng = 0
        else:
            ng = s.find("g")
        for chr in s[-1::-1]:
            if chr == "g":
                ng = 0
            else:
                ng += 1
            if chr == c:
                ans = max(ans, ng)
        print(ans)


if __name__ == "__main__":
    main()
