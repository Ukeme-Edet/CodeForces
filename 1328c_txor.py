from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = input()
        ans1, ans2 = "", ""
        b1 = False
        for i in range(n):
            if x[i] == "2":
                if not b1:
                    ans1 += "1"
                    ans2 += "1"
                else:
                    ans1 += "0"
                    ans2 += "2"
            elif x[i] == "1":
                if not b1:
                    ans1 += "1"
                    ans2 += "0"
                    b1 = True
                else:
                    ans1 += "0"
                    ans2 += "1"
            else:
                ans1 += "0"
                ans2 += "0"
        print(f"{ans1}\n{ans2}")


if __name__ == "__main__":
    main()
