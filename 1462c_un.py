from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        if x > 45:
            print(-1)
            continue
        ans = []
        for i in range(9, 0, -1):
            if x <= i:
                ans.insert(0, x)
                break
            ans.insert(0, i)
            x -= i
        print("".join([str(x) for x in ans]))


if __name__ == "__main__":
    main()
