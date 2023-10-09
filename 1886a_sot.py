from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 7:
            print("NO")
        else:
            if n % 3 == 0:
                if len(set([1, 4, n - 5])) == 3 and n - 5 % 3 != 0 and n - 5 > 0:
                    print("YES")
                    print(f"1 4 {n - 5}")
                else:
                    print("NO")
            else:
                print("YES")
                print(f"1 2 {n - 3}")


if __name__ == "__main__":
    main()
