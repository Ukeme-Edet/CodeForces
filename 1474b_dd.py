from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    primes = seive(1000000)
    for _ in range(t):
        d = int(input())
        res = []
        last = 1
        for i in range(len(primes)):
            if primes[i] - last >= d:
                res.append(primes[i])
                last = primes[i]
                if len(res) == 2:
                    break
        print(res[0] * res[1])


def seive(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False
    return [i for i in range(n + 1) if prime[i]]


if __name__ == "__main__":
    main()
