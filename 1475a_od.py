from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 3:
            print("NO")
        elif n % 2 == 1:
            print("YES")
        elif n % 2 == 0:
            while n % 2 == 0 and n != 2:
                n //= 2
            if n % 2 == 1:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


if __name__ == "__main__":
    main()
