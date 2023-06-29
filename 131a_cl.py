from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s = input()
    print(s.swapcase() if (s[0].islower() and s[1:].isupper())
          or s.isupper() or s[1:] == "" else s)


if __name__ == "__main__":
    main()
