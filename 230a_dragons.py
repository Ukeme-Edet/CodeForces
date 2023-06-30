from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s, n = map(int, input().split())
    dragons = []
    for _ in range(n):
        dragons.append(list(map(int, input().split())))
    dragons.sort(key=lambda x: x[0])
    for i in range(n):
        if not s > dragons[i][0]:
            print("NO")
            return
        s += dragons[i][1]
    print("YES")


if __name__ == "__main__":
    main()
