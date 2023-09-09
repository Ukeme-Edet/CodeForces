from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    q = int(input())
    for _ in range(q):
        s = input()
        t = input()
        if s[0] != t[0] or s[-1] != t[-1] or set(s) != set(t):
            print(-1)
            continue
        slcm = lcm(len(s), len(t))
        if s * (slcm // len(s)) == t * (slcm // len(t)):
            print(s * (slcm // len(s)))
        else:
            print(-1)


def gdc(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gdc(a, b)


if __name__ == "__main__":
    main()
