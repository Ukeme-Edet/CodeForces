from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        nums = sorted([int(x) for x in input().split()])
        print("YES" if nums[0] + nums[1] == nums[2] else "NO")


if __name__ == "__main__":
    main()
