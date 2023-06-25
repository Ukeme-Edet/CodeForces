from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s = input()
    subsequent = 0
    for i in range(len(s)):
        if s[i] != s[i-1]:
            subsequent = 0
            continue
        subsequent += 1
        if subsequent == 6:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
