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
        permutation = set()
        permutation.add(a[0])
        for i in range(1, len(a)):
            c = a[i] - a[i - 1]
            if c in permutation:
                for j in range(1, c // 2 + 1):
                    if not (j in permutation or c - j in permutation) and len(permutation) < n - 1:
                        permutation.add(j)
                        permutation.add(c - j)
                        break
                else:
                    print("NO")
                    break
            else:
                permutation.add(c)
        else:
            print("YES")


if __name__ == "__main__":
    main()
