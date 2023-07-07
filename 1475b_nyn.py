from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 2020:
            print("NO")
        else:
            l, r = n // 2020, 0
            while r <= n // 2021:
                if l * 2020 + r * 2021 == n:
                    print("YES")
                    break
                else:
                    l -= 1
                    r += 1
            else:
                print("NO")


if __name__ == "__main__":
    main()
