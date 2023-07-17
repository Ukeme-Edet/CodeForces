from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        a.sort()
        as_l = len(set(a)) - 1
        longest_s = find_longest(a)
        print(max(min(as_l, longest_s), min(as_l + 1, longest_s - 1)))


def find_longest(a):
    longest = 0
    longest_c = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            longest_c += 1
        else:
            longest_c = 1
        longest = max(longest, longest_c)
    return longest


if __name__ == "__main__":
    main()
