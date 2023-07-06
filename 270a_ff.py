from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    angles = [60, 90, 108, 120, 135, 140, 144, 150, 156, 160, 162,
              165, 168, 170, 171, 172, 174, 175, 176, 177, 178, 179]
    for _ in range(t):
        a = int(input())
        if a < 60:
            print("NO")
        else:
            if a in angles:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
