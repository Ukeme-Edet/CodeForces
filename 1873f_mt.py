from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        h = [int(x) for x in input().split()]
        sub_arrs = []
        i = longest = 0
        while i < n - 1:
            sub = [i, 0]
            while i < n - 1 and h[i] % h[i + 1] == 0:
                i += 1
                sub[1] = i
            sub_arrs.append(sub)
            i += 1
            if i < n and a[i] <= k:
                longest = 1
        if i < n and a[i] <= k:
            longest = 1
        for sub in sub_arrs:
            if sum(a[sub[0]: sub[1] + 1]) <= k:
                longest = max(longest, sub[1] - sub[0] + 1)
            else:
                i = sub[0]
                sf = 0
                last = i
                while i <= sub[1]:
                    while i <= sub[1] and sf + a[i] <= k:
                        sf += a[i]
                        i += 1
                    longest = max(longest, i - last)
                    if i <= sub[1]:
                        while sf + a[i] > k:
                            sf -= a[last]
                            last += 1
                    else:
                        break
        print(longest)


if __name__ == "__main__":
    main()
