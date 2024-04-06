from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        if s.count("1") % 2:
            print("NO")
            continue
        if s.count("1") == 2 and s.find("11") != -1:
            print("NO")
            continue
        print("YES")


if __name__ == "__main__":
    main()
