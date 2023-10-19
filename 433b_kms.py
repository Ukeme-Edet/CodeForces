from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    u = sorted(v)
    vdp = [0] * (n + 1)
    udp = [0] * (n + 1)
    for i in range(1, n + 1):
        vdp[i] = v[i - 1] + vdp[i - 1]
        udp[i] = u[i - 1] + udp[i - 1]
    m = int(input())
    for _ in range(m):
        t, l, r = [int(x) for x in input().split()]
        c = udp if t - 1 else vdp
        print(c[r] - c[l - 1])


if __name__ == "__main__":
    main()
