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
		ps = [0] * (n + 1)
		for i in range(n):
			ps[i + 1] = ps[i] + a[i]
		md = 0
		for k in range(1, n // 2 + 1):
			if n % k:
				continue
			maxw, minw = -float("inf"), float("inf")
			for i in range(n // k):
				maxw = max(maxw, ps[(i + 1) * k] - ps[i * k])
				minw = min(minw, ps[(i + 1) * k] - ps[i * k])
			md = max(md, maxw - minw)
		print(md)


if __name__ == "__main__":
	main()
