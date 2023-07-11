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
        max_cwo, open = 0, 0
        for i in range(n):
            if s[i] == "(":
                open += 1
            else:
                open -= 1
            if open < 0:
                max_cwo = max(max_cwo, -open)
        print(max_cwo)


if __name__ == "__main__":
    main()
