from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        start = ".."
        other = "##"
        for i in range(n):
            row = ""
            temp = start
            start = other
            other = temp
            for j in range(n):
                if j % 2:
                    row += other
                else:
                    row += start
            print(row)
            print(row)


if __name__ == "__main__":
    main()
