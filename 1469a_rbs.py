from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if s[0] != ')' and s[-1] !=
              '(' and len(s) % 2 == 0 else "NO")


if __name__ == "__main__":
    main()
