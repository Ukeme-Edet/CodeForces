from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([int(x) for x in input().split()], reverse=True)
        gs = turn = 0
        for i in range(n):
            if a[i] % 2 and turn:
                gs -= a[i]
            elif not (a[i] % 2 or turn):
                gs += a[i]
            turn ^= 1
        print("Tie" if gs == 0 else "Alice" if gs > 0 else "Bob")


if __name__ == "__main__":
    main()
