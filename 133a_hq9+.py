from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    p = input()
    print("YES" if "H" in p or "Q" in p or "9" in p else "NO")


if __name__ == "__main__":
    main()
