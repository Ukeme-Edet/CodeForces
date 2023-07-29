from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = input()
    c114, c14, c1 = n.count("144"), n.count("14"), n.count("1")
    print("YES" if (c114 * 3) + ((c14 - c114) * 2) +
          (c1 - c14) == len(n) else "NO")


if __name__ == "__main__":
    main()
