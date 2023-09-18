from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        max_d = d = 0
        for c in s:
            if c == "L":
                d += 1
            else:
                max_d = max(max_d, d)
                d = 0
        max_d = max(max_d, d)
        print(max_d + 1)


if __name__ == "__main__":
    main()
