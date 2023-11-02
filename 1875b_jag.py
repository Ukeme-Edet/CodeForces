from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        xma, xmi = max(max(a), max(b)), min(min(a), min(b))
        abg, asm = max(a) > max(b), min(a) < min(b)
        if k % 2 == 1:
            if k > 1:
                print(sum(a) - xmi + xma)
            else:
                print(sum(a) - min(a) + max(b) if n > 1 else a[0])
        else:
            res = sum(a)
            if abg:
                res += max(b)
            if not asm:
                res += min(b) - min(a)
            print(res)


if __name__ == "__main__":
    main()