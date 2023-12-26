from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    print("IGNORE HIM!" if len(set(input())) % 2 else "CHAT WITH HER!")


if __name__ == "__main__":
    main()
