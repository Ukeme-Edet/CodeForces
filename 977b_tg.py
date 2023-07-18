from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    s = input()
    tgf = {}
    for i in range(n-1):
        if s[i:i+2] in tgf:
            tgf[s[i:i+2]] += 1
        else:
            tgf[s[i:i+2]] = 1
    tgf = sorted([x for x in tgf.items()], key=lambda x: -x[1])
    print(tgf[0][0])


if __name__ == "__main__":
    main()
