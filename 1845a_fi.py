from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        if n % 2 == 0:
            if k > 1:
                print("YES")
                if x == 1:
                    print(n // 2)
                    print(("2 " * (n // 2)).strip())
                    continue
                print(n)
                print(("1 " * n).strip())
                continue
            else:
                print("NO")
                continue
        if x == 1:
            if k > 2:
                print("YES")
                print(n // 2)
                print("2 " * ((n // 2) - 1) + "3")
                continue
            print("NO")
            continue
        print("YES")
        print(n)
        print((("1 ") * n).strip())


if __name__ == "__main__":
    main()
