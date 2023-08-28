from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        cubes = {i ** 3 for i in range(1, 10000)}
        for a in cubes:
            if x - a in cubes:
                print("YES")
                break
        else:
            print("NO")


if __name__ == "__main__":
    main()
