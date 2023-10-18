from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([bin(int(x)) for x in input().split()])
        ep = [bin(x) for x in sorted([x + 1 for x in range(n)], reverse=True)]
        for i in range(n):
            for aj in a:
                if ep[i] in aj:
                    a.remove(aj)
                    break
            else:
                break
        else:
            print("YES")
            continue
        print("NO")


if __name__ == "__main__":
    main()
