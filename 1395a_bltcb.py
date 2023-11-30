from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        r, g, b, w = [int(_) for _ in input().split()]
        if r % 2 + g % 2 + b % 2 + w % 2 < 2:
            print("Yes")
        elif r > 0 and g > 0 and b > 0:
            r -= 1
            g -= 1
            b -= 1
            w += 3
            if r % 2 + g % 2 + b % 2 + w % 2 < 2:
                print("Yes")
            else:
                print("No")
        else:
            print("No")


if __name__ == "__main__":
    main()
