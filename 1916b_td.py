from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b = [int(_) for _ in input().split()]
        for i in range(b ** 2, a ** 2 + 1, -b):
            facs = []
            for j in range(int(i ** 0.5) + 1, 0, -1):
                if not i % j:
                    facs.append(j)
                if len(facs) > 1:
                    break
            if len(facs) > 1 and facs[0] == b and facs[1] == a:
                print(i)
                break


if __name__ == "__main__":
    main()
