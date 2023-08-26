from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(-1)
            continue
        s = "9" * (n - 1) + "8"
        while is_invalid(s[-4300:]):
            s = s[:-4300] + str(int(s[-4300:]) - 1)
        print(s)


def is_invalid(s):
    ss = set(s)
    for digit in ss:
        if int(s) % int(digit) == 0:
            return True
    return "0" in ss


if __name__ == "__main__":
    main()
