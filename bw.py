from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = map(int, input().split())
    hash_map = [0] * 100001
    v = [[int(x) for x in input().split()] for _ in range(n)]
    for b in v:
        hash_map[b[0]:b[1] + 1] = [x + 1 for x in hash_map[b[0]:b[1] + 1]]
    for _ in range(m):
        c, d = map(int, input().split())
        print(sum(hash_map[c:d+1]))


if __name__ == "__main__":
    main()
