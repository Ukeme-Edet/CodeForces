from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        grid = [set(input()) for _ in range(3)]
        for row in grid:
            if "?" in row:
                print("A" if "A" not in row else "B" if "B" not in row else "C")
                break


if __name__ == "__main__":
    main()
