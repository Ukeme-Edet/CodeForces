from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    print(input().replace("WUB", " ").strip())


if __name__ == "__main__":
    main()
