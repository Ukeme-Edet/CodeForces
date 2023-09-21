from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        ss = sorted(s)
        if all(s[i] != ss[i] for i in range(len(s))):
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()
