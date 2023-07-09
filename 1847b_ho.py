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
        st = a[0]
        for ai in a:
            st &= ai
        if st > 0 or n == 1:
            print(1)
            continue
        l, r = 0, 0
        groups = 0
        while r < n:
            st = a[r]
            while r < n and st & a[r] != 0:
                st &= a[r]
                r += 1
            if r < n and st & a[r] == 0:
                groups += 1
                l = r
                r += 1
        print(groups)


if __name__ == "__main__":
    main()
