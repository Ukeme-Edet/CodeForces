from collections import defaultdict
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
        mm = defaultdict(list)
        for ai in a:
            mm[str(ai % k)].append(ai)
        if sum(len(v) % 2 for v in mm.values()) > n % 2:
            print(-1)
            continue
        res = 0
        for v in mm.values():
            v.sort()
            if not len(v) % 2:
                for i in range(1, len(v), 2):
                    res += v[i] - v[i - 1]
            else:
                ls, rs = [0] * ((len(v) + 1) // 2), [0] * ((len(v) + 1) // 2)
                l = r = 0
                for i in range(1, len(v), 2):
                    ls[i // 2] = l
                    rs[len(v) // 2 - i // 2] = r
                    l += v[i] - v[i - 1]
                    r += v[len(v) - i] - v[len(v) - i - 1]
                ls[len(v) // 2] = l
                rs[0] = r
                res += min(ls[i] + rs[i] for i in range((len(v) + 1) // 2))
        print(res // k)


if __name__ == "__main__":
    main()
