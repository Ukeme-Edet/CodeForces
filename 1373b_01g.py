from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("DA" if min(s.count("1"), s.count("0")) % 2 == 1 else "NET")


if __name__ == "__main__":
    main()
