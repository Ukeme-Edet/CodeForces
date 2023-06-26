from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s = input()
    hello = "hello"
    i = 0
    for c in s:
        if c == hello[i]:
            i += 1
        if i == 5:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
