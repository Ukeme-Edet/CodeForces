from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _ = int(input())
    off = un = 0
    events = [int(x) for x in input().split()]
    for event in events:
        if event == -1:
            if off:
                off -= 1
            else:
                un += 1
        else:
            off += event
    print(un)


if __name__ == "__main__":
    main()
