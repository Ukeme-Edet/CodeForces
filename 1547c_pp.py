from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        input()
        k, n, m = [int(_) for _ in input().split()]
        a = [int(_) for _ in input().split()]
        b = [int(_) for _ in input().split()]
        cs = []
        ap, bp = 0, 0
        while ap < n or bp < m:
            if ap < n and bp < m:
                if a[ap] < 1:
                    cs.append(a[ap])
                    k += 1
                    ap += 1
                elif b[bp] < 1:
                    cs.append(b[bp])
                    k += 1
                    bp += 1
                elif a[ap] <= k:
                    cs.append(a[ap])
                    ap += 1
                elif b[bp] <= k:
                    cs.append(b[bp])
                    bp += 1
                else:
                    break
            elif ap < n:
                if a[ap] < 1 or a[ap] <= k:
                    cs.append(a[ap])
                    if a[ap] < 1:
                        k += 1
                    ap += 1
                else:
                    break
            else:
                if b[bp] < 1 or b[bp] <= k:
                    cs.append(b[bp])
                    if b[bp] < 1:
                        k += 1
                    bp += 1
                else:
                    break
        print(" ".join([str(_) for _ in cs]) if ap == n and bp == m else -1)


if __name__ == "__main__":
    main()
