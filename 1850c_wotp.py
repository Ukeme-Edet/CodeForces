from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        word = ""
        for i in range(8):
            l = [x for x in input() if x != "."]
            if l:
                word += l[0]
        print(word)


if __name__ == "__main__":
    main()
