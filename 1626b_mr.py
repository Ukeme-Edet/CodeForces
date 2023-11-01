from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x = input()
        for i in range(len(x) - 1):
            if int(x[-i-1]) + int(x[-i-2]) > 9:
                res = x[:-i-2] + str(int(x[-i-1]) + int(x[-i-2]))
                if i > 0:
                    res += x[-i:]
                print(res)
                break
        else:
            print(str(int(x[0]) + int(x[1])) + x[2:])


if __name__ == "__main__":
    main()
