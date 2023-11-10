from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a, b = input(), input()
    c = int(a) + int(b)
    print("YES" if int(str(c).replace("0", "")) == int(
        a.replace("0", "")) + int(b.replace("0", "")) else "NO")


if __name__ == "__main__":
    main()
