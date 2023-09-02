from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    g = input()
    g += input()
    s = input()
    if sorted(g) == sorted(s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
