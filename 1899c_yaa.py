from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(_) for _ in input().split()]
        l = r = 0
        msum = -float("inf")
        while r < n:
            r += 1
            pp = a[l] % 2
            while r < n and a[r] % 2 != pp:
                pp = a[r] % 2
                r += 1
            msum = max(msum, max_sub_sum(a[l:r]))
            l = r
        print(msum)


def max_sub_sum(arr):
    max_so_far = -float("inf")
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far


if __name__ == "__main__":
    main()
